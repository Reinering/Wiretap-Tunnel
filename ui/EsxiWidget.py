#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module implementing LinuxWidget.
author: Reiner New
email: nbxlc@hotmail.com
"""

from PySide6.QtCore import Slot, QCoreApplication, QThread, Signal, QSize
from PySide6.QtWidgets import QWidget
import os
import subprocess
# 进程管理信号
import signal
import psutil
import logging

from .Ui_EsxiWidget import Ui_EsxiWidget
from .components.tip import Tip
from .components.combo_box import MSEComboBox
from manage import SETTINGS, EncodingFormat, os_platform, LOGLEVEL, PlinkFile
from common.ssh import SSH
from .utils.config import saveConfig


class EsxiWidget(QWidget, Ui_EsxiWidget):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super().__init__(parent)
        self.setupUi(self)
        self.translate = QCoreApplication.translate
        self.interfaces = {}

        self.initWidget()

        self.auth = None
        self.protocol = 'ssh'
        self.getTh = GetThread()
        self.getTh.out_signal.connect(self.setInfo)

        self.processTh = ProcessThread()
        self.processTh.out_signal.connect(self.setCaptureInfo)

    def initWidget(self):
        # init setting
        self.EditableComboBox_host.addItems(SETTINGS["esxi"]["host"])
        self.EditableComboBox_port.addItems(SETTINGS["esxi"]["port"])
        self.EditableComboBox_username.addItems(SETTINGS["esxi"]["user"])
        self.EditableComboBox_password.addItems(SETTINGS["esxi"]["password"])

        self.EditableComboBox_host.setCurrentIndex(-1)
        self.EditableComboBox_port.setCurrentIndex(-1)
        self.EditableComboBox_username.setCurrentIndex(-1)
        self.EditableComboBox_password.setCurrentIndex(-1)
        self.EditableComboBox_tcpdump.setCurrentIndex(-1)
        self.MSECComboBox_pktcap.setCurrentIndex(-1)

        self.EditableComboBox_tcpdump.setPlaceholderText("选择参数或输入参数")
        self.EditableComboBox_tcpdump.addItems(SETTINGS["esxi"]["tcpdump"])
        self.MSECComboBox_pktcap.setPlaceholderText("选择参数或输入参数")
        self.MSECComboBox_pktcap.addItems(SETTINGS["pktcap-uw"])
        self.MSECComboBox_pktcap.setItemReadOnly('capture', True)
        self.MSECComboBox_pktcap.setItemReadOnly('dir', True)


        self.EditableComboBox_tcpdump.setEnabled(False)
        self.MSECComboBox_pktcap.setEnabled(False)
        self.ComboBox_interface.setEnabled(False)
        self.groupBox_cmd.setEnabled(False)

    def setInfo(self, p0):
        if not p0:
            return

        if p0[0] == "log":
            self.textBrowser.setText(p0[1])
        elif p0[0] == "interfaces":
            if p0[1]:
                self.ComboBox_interface.clear()
                self.interfaces.clear()
                self.ComboBox_interface.setEnabled(True)
                self.groupBox_cmd.setEnabled(True)
            p0[1].pop(0)
            SETTINGS["pktcap-uw"]["switchport"].clear()
            for inter in p0[1]:
                if not inter:
                    continue
                tmp = inter.split(' ')
                self.interfaces[tmp[0]] = tmp[1]
                self.ComboBox_interface.addItem(tmp[1], userData=tmp[0])
                SETTINGS["pktcap-uw"]["switchport"].append(tmp[0])

            self.ComboBox_interface.setCurrentIndex(-1)
        elif p0[0] == "error":
            Tip.error(self, self, content=p0[1])
            self.PrimaryPushButton_start.setEnabled(False)
        elif p0[0] == "warn":
            Tip.warning(self, self, content=p0[1])
            self.PrimaryPushButton_start.setEnabled(False)
        elif p0[0] == "info":
            Tip.info(self, self, content=p0[1])
            self.PrimaryPushButton_start.setEnabled(False)
        elif p0[0] == "finish":
            self.PrimaryPushButton_connect.setEnabled(True)
        elif p0[0] == "auth":
            if p0[1]["host"] not in SETTINGS["esxi"]["host"]:
                SETTINGS["esxi"]["host"].append(p0[1]["host"])
            if p0[1]["port"] not in SETTINGS["esxi"]["port"]:
                SETTINGS["esxi"]["port"].append(p0[1]["port"])
            if p0[1]["user"] not in SETTINGS["esxi"]["user"]:
                SETTINGS["esxi"]["user"].append(p0[1]["user"])
            if p0[1]["password"] not in SETTINGS["esxi"]["password"]:
                SETTINGS["esxi"]["password"].append(p0[1]["password"])

            self.auth = p0[1]
            saveConfig()
            self.PrimaryPushButton_start.setEnabled(True)
        elif p0[0] == "cmd":
            print(p0[1])

    def setCaptureInfo(self, p0):
        if not p0:
            return

        if p0[0] == "stop":
            self.setState(False)
            self.textBrowser.append(p0[1])
        elif p0[0] == "log":
            self.textBrowser.append(p0[1])

    def setState(self, checked):
        if checked:
            self.PrimaryPushButton_start.setText("Stop")
            self.groupBox_ssh.setEnabled(False)

            self.PrimaryPushButton_connect.setEnabled(False)
            self.ComboBox_interface.setEnabled(False)
            self.groupBox_cmd.setEnabled(False)
            self.PrimaryPushButton_clear.setEnabled(False)
        else:
            self.PrimaryPushButton_start.setText("Start")
            self.groupBox_ssh.setEnabled(True)

            self.PrimaryPushButton_connect.setEnabled(True)
            self.ComboBox_interface.setEnabled(True)
            self.groupBox_cmd.setEnabled(True)
            self.PrimaryPushButton_clear.setEnabled(True)

    @Slot(bool)
    def on_RadioButton_tcpdump_clicked(self, checked):
        """
        Slot documentation goes here.

        @param checked DESCRIPTION
        @type bool
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.EditableComboBox_tcpdump.setEnabled(checked)
        self.MSECComboBox_pktcap.setEnabled(not checked)

    @Slot(bool)
    def on_RadioButton_pktcap_clicked(self, checked):
        """
        Slot documentation goes here.

        @param checked DESCRIPTION
        @type bool
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.MSECComboBox_pktcap.setEnabled(checked)
        self.EditableComboBox_tcpdump.setEnabled(not checked)

    @Slot()
    def on_PrimaryPushButton_clear_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.EditableComboBox_host.setCurrentIndex(-1)
        self.EditableComboBox_port.setCurrentIndex(-1)
        self.EditableComboBox_username.setCurrentIndex(-1)
        self.EditableComboBox_password.setCurrentIndex(-1)
        self.EditableComboBox_tcpdump.setCurrentIndex(-1)
        self.MSECComboBox_pktcap.setCurrentIndex(-1)
        self.ComboBox_interface.clear()

    @Slot()
    def on_PrimaryPushButton_connect_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError

        host = self.EditableComboBox_host.currentText()
        if not host:
            Tip.warning(self, self.EditableComboBox_host, content="host is empty")
            return
        port = self.EditableComboBox_port.currentText()
        if not port:
            Tip.warning(self, self.EditableComboBox_port, content="port is empty")
            return
        username = self.EditableComboBox_username.currentText()
        if not username:
            Tip.warning(self, self.EditableComboBox_username, content="username is empty")
            return
        password = self.EditableComboBox_password.currentText()
        if not password:
            Tip.warning(self, self.EditableComboBox_password, content="password is empty")
            return

        self.getTh.setParams(host=host, port=port, user=username, password=password)

        self.getTh.start()
        self.PrimaryPushButton_connect.setEnabled(False)

    @Slot()
    def on_PrimaryPushButton_start_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        if self.PrimaryPushButton_start.text() == "Start":

            if not self.auth:
                Tip.warning(self, self.PrimaryPushButton_start, content="请先点击'Connect', 确认连接正常，选择正确接口后，再点击'Start'")
                return

            interface = self.ComboBox_interface.currentText()


            wiresharkPath = SETTINGS["default"]["wiresharkPath"]
            if not SETTINGS["default"]["wiresharkPath"]:
                wiresharkPath = 'wireshark'

            if self.RadioButton_tcpdump.isChecked():
                if not interface:
                    Tip.warning(self, self.groupBox_cmd, content="interface 不能为空")
                    return
                params = self.EditableComboBox_tcpdump.currentText()

                cmd = '{} -{} {}@{} -P {} -pw {} "tcpdump-uw -i {} {} -s 0 -l -w -" ' \
                      '| "{}" -k -i -'.format(PlinkFile,
                                              self.protocol,
                                              self.auth["user"],
                                              self.auth["host"],
                                              self.auth["port"],
                                              self.auth["password"],
                                              interface,
                                              params,
                                              wiresharkPath
                                              )
            elif self.RadioButton_pktcap.isChecked():
                datas = self.MSECComboBox_pktcap.itemDatas()
                params = ''

                if "vmnic" in interface:
                    params += '--uplink {} '.format(interface)
                elif "vmk" in interface:
                    params += '--vmk {} '.format(interface)
                else:
                    pass

                for key, value in datas.items():
                    if not value:
                        self.textBrowser.append(f"{key} 参数不能为空")
                        continue
                    if key == "other":
                        params += value + ' '
                    elif "-" not in key:
                        if len(key) == 1:
                            params += '-' + key + ' ' + value + ' '
                        else:
                            params += '--' + key + ' ' + value + ' '
                    else:
                        params += key + ' ' + value + ' '
                
                if not params:
                    Tip.warning(self, self.groupBox_cmd, content="参数不能为空")
                    return

                cmd = '{} -{} {}@{} -P {} -pw {} "pktcap-uw {} -o -" ' \
                      '| "{}" -k -i -'.format(PlinkFile,
                                              self.protocol,
                                              self.auth["user"],
                                              self.auth["host"],
                                              self.auth["port"],
                                              self.auth["password"],
                                              params,
                                              wiresharkPath
                                              )
            else:
                Tip.warning(self, self.groupBox_cmd, content="请选择抓包工具")
                return

            if LOGLEVEL <= 2:
                self.textBrowser.append(cmd)
            self.processTh.setParams(self.protocol, cmd, self.auth["password"])
            self.processTh.start()
            self.setState(True)
        elif self.PrimaryPushButton_start.text() == "Stop":
            self.processTh.stop()


class GetThread(QThread):
    out_signal = Signal(tuple)

    def __init__(self):
        super(GetThread, self).__init__()
        self.stopBool = False

    def setParams(self, **kwargs):
        self.kwargs = kwargs

    def run(self):
        ssh = SSH()
        try:
            ssh.authSSH(self.kwargs['host'], self.kwargs['port'], self.kwargs['user'], self.kwargs['password'])
        except Exception as e:
            self.out_signal.emit(("error", "连接失败：" + str(e)))
            self.out_signal.emit(("finish", ''))
            return
        except OSError as e:
            self.out_signal.emit(("error", "连接失败：" + str(e)))
            self.out_signal.emit(("finish", ''))
            return

        self.out_signal.emit(("log", "连接成功"))

        stdin, stdout, stderr = ssh.exec_cmd(
            """net-stats -l | awk '{print $1, $NF}'""")
        # """ls -l /sys/class/net/ | sed '1d' | awk 'BEGIN {FS="/"} {print $NF}'"""
        # """cat /proc/net/dev | awk '{i++; if(i>2){print $1}}' | sed 's/^[\\t]*//g' | sed 's/[:]*$//g'"""

        out = stdout.read().decode()
        err = stderr.read().decode()

        if out:
            self.out_signal.emit(("log", out))
            self.out_signal.emit(("interfaces", out.split('\n')))
            self.out_signal.emit(
                ("auth", {"host": self.kwargs['host'], "port": self.kwargs['port'],
                          "user": self.kwargs['user'], "password": self.kwargs['password']}))
        elif err:
            self.out_signal.emit(("log", err))

        ssh.close()

        self.out_signal.emit(("finish", ''))

    def stop(self):
        self.stopBool = True


class ProcessThread(QThread):
    out_signal = Signal(tuple)

    def __init__(self):
        super(ProcessThread, self).__init__()
        self.stopBool = False

    def setParams(self, protocol, cmd, password):
        self.protocol = protocol
        self.cmd = cmd
        self.password = password

    def stop(self):
        self.stopBool = True
        try:
            if "windows" in os_platform.lower():
                # self.out_signal.emit(("stop", "抓包已关闭"))

                # os.killpg(os.getpgid(self.p.pid), signal.SIGHUP)
                # os.killpg(os.getpgid(self.p.pid), signal.SIGTERM)
                if LOGLEVEL > 2:
                    self.out_signal.emit(("stop", "抓包已关闭"))
                    # self.p.send_signal(signal.CTRL_C_EVENT)
                    os.kill(0, signal.CTRL_C_EVENT)
                else:
                    # subprocess.run("taskkill -f -im Wireshark*", shell=True)
                    self.kill(self.p.pid)
        except Exception as e:
            print(e)
            # logging.error(e)

    def kill(self, proc_pid):
        # kill process with subprocess
        kill_proc = subprocess.Popen(
            "TASKKILL /F /PID {pid} /T".format(pid=proc_pid),
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)

    def run(self):
        self.stopBool = False

        if not self.cmd:
            self.out_signal.emit(("log", "命令参数不正确"))
            return
        print(self.cmd)
        try:
            self.p = subprocess.Popen(self.cmd,
                                      stdin=subprocess.PIPE,
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.STDOUT,
                                      shell=True)

            for line in iter(self.p.stdout.readline, 'b'):
                if self.stopBool:
                    raise Exception('ProcessThread stop')
                elif not line:
                    continue
                line = line.decode(EncodingFormat)
                if self.protocol == 'ssh' and 'Store key in cache? (y/n, Return cancels connection, i for more info)' in line:
                    self.p.stdin.write(bytes('n\r\n', EncodingFormat))
                    self.p.stdin.flush()
                elif 'Password:' in line:
                    self.p.stdin.write(bytes(self.password + '\r\n', EncodingFormat))
                    self.p.stdin.flush()
                elif 'tcpdump: listening on' in line:
                    self.out_signal.emit(("log", "抓包开启中......"))
                elif "Capture started" in line:
                    self.out_signal.emit(("cmd", self.cmd))
                elif 'Connection abandoned' in line:
                    raise Exception('ProcessThread exit')
                elif "不是内部或外部命令，也不是可运行的程序" in line:
                    raise Exception('ProcessThread fail')
                elif 'Capture Start failed' in line:
                    raise Exception('ProcessThread fail')
                elif '系统找不到指定的路径' in line or 'The system cannot find the path specified' in line:
                    raise Exception('ProcessThread fail')
                elif 'Connection abandoned' in line or 'Capture stopped' in line:
                    raise Exception('ProcessThread fail')
                elif 'tcpdump: not found' in line:
                    self.out_signal.emit(("error", "tcpdump 未安装"))
                else:
                    self.out_signal.emit(("log", line))

        except Exception as e:
            print(e)
            self.p.kill()

        self.out_signal.emit(("stop", "抓包已关闭"))
