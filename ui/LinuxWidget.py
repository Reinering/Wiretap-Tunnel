#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module implementing LinuxWidget.
author: Reiner New
email: nbxlc@hotmail.com
"""

from PySide6.QtCore import Slot, QCoreApplication, QThread, Signal
from PySide6.QtWidgets import QWidget
import os
import subprocess
# 进程管理信号
import signal
import psutil
import logging

from .Ui_LinuxWidget import Ui_LinuxWidget
from .components.tip import Tip
from manage import SETTINGS, EncodingFormat, os_platform, LOGLEVEL, PlinkFile
from common.ssh import SSH
from .utils.config import saveConfig


class LinuxWidget(QWidget, Ui_LinuxWidget):
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
        self.interfaces = ['']
        self.containers = ['']

        self.initWidget()

        self.auth = None
        self.protocol = 'ssh'
        self.getTh = GetThread()
        self.getTh.out_signal.connect(self.setInfo)

        self.processTh = ProcessThread()
        self.processTh.out_signal.connect(self.setCaptureInfo)

    def initWidget(self):
        # init setting
        self.EditableComboBox_host.addItems(SETTINGS["linux"]["host"])
        self.EditableComboBox_port.addItems(SETTINGS["linux"]["port"])
        self.EditableComboBox_username.addItems(SETTINGS["linux"]["user"])
        self.EditableComboBox_password.addItems(SETTINGS["linux"]["password"])
        self.EditableComboBox_su_username.addItems(SETTINGS["linux"]["su_user"])
        self.EditableComboBox_su_password.addItems(SETTINGS["linux"]["su_password"])
        self.EditableComboBox_cmd.addItems(SETTINGS["linux"]["cmd"])

        self.CheckBox_sudo.setMinimumWidth(65)
        self.CheckBox_su.setMinimumWidth(45)
        self.CheckBox_docker.setMinimumWidth(70)

        self.EditableComboBox_host.setCurrentIndex(-1)
        self.EditableComboBox_port.setCurrentIndex(-1)
        self.EditableComboBox_username.setCurrentIndex(-1)
        self.EditableComboBox_password.setCurrentIndex(-1)
        self.EditableComboBox_su_username.setCurrentIndex(-1)
        self.EditableComboBox_su_password.setCurrentIndex(-1)
        self.EditableComboBox_cmd.setCurrentIndex(-1)

        self.ComboBox_interface.addItems(self.interfaces)
        self.EditableComboBox_container.addItems(self.containers)

        self.EditableComboBox_su_username.setEnabled(False)
        self.EditableComboBox_su_password.setEnabled(False)
        self.EditableComboBox_container.setEnabled(False)
        self.ComboBox_interface.setEnabled(False)
        self.EditableComboBox_cmd.setEnabled(False)
        self.PrimaryPushButton_start.setEnabled(False)

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
                self.EditableComboBox_cmd.setEnabled(True)
            for inter in p0[1]:
                if not inter:
                    continue
                self.interfaces.append(inter)
            self.ComboBox_interface.addItems(self.interfaces)
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
            if p0[1]["host"] not in SETTINGS["linux"]["host"]:
                SETTINGS["linux"]["host"].append(p0[1]["host"])
            if p0[1]["port"] not in SETTINGS["linux"]["port"]:
                SETTINGS["linux"]["port"].append(p0[1]["port"])
            if p0[1]["user"] not in SETTINGS["linux"]["user"]:
                SETTINGS["linux"]["user"].append(p0[1]["user"])
            if p0[1]["password"] not in SETTINGS["linux"]["password"]:
                SETTINGS["linux"]["password"].append(p0[1]["password"])
            if p0[1]["su"]:
                if p0[1]["user_su"] and p0[1]["user_su"] not in SETTINGS["linux"]["user_su"]:
                    SETTINGS["linux"]["user_su"].append(p0[1]["user_su"])
                if p0[1]["password_su"] not in SETTINGS["linux"]["password_su"]:
                    SETTINGS["linux"]["password_su"].append(p0[1]["password_su"])

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

            self.groupBox_interface.setEnabled(False)

            self.PrimaryPushButton_clear.setEnabled(False)
        else:
            self.PrimaryPushButton_start.setText("Start")
            self.groupBox_ssh.setEnabled(True)
            self.PrimaryPushButton_connect.setEnabled(True)
            self.groupBox_interface.setEnabled(True)
            self.PrimaryPushButton_clear.setEnabled(True)

    @Slot(bool)
    def on_CheckBox_su_clicked(self, checked):
        """
        Slot documentation goes here.

        @param checked DESCRIPTION
        @type bool
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.EditableComboBox_su_username.setEnabled(checked)
        self.EditableComboBox_su_password.setEnabled(checked)

    @Slot(bool)
    def on_CheckBox_docker_clicked(self, checked):
        """
        Slot documentation goes here.

        @param checked DESCRIPTION
        @type bool
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.EditableComboBox_container.setEnabled(checked)

    @Slot()
    def on_PrimaryPushButton_clear_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.EditableComboBox_host.setCurrentIndex(0)
        self.EditableComboBox_port.setCurrentIndex(0)
        self.EditableComboBox_username.setCurrentIndex(0)
        self.EditableComboBox_password.setCurrentIndex(0)
        self.EditableComboBox_su_username.setCurrentIndex(0)
        self.EditableComboBox_su_password.setCurrentIndex(0)
        self.EditableComboBox_container.setCurrentIndex(0)
        self.ComboBox_interface.setCurrentIndex(0)
        self.EditableComboBox_cmd.setCurrentIndex(0)
        self.ComboBox_interface.clear()
        self.EditableComboBox_container.clear()

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

        su = self.CheckBox_su.isChecked()
        if su:
            su_username = self.EditableComboBox_su_username.currentText()
            if not su_username:
                Tip.warning(self, self.EditableComboBox_su_username, content="su username is empty")
                return
            su_password = self.EditableComboBox_su_password.currentText()
            if not su_password:
                Tip.warning(self, self.EditableComboBox_su_password, content="su password is empty")
                return
            self.getTh.setParams(host=host, port=port, user=username, password=password, su=su,
                                 user_su=su_username, password_su=su_password)
        else:
            self.getTh.setParams(host=host, port=port, user=username, password=password, su=su)

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

            if not interface:
                Tip.warning(self, self.ComboBox_interface, content="interface 不能为空")
                return

            params = self.EditableComboBox_cmd.currentText()
            # if not params:
                # Tip.warning(self, self.EditableComboBox_cmd, content="CMD 不能为空")
            #     return
            wiresharkPath = SETTINGS["default"]["wiresharkPath"]
            if not SETTINGS["default"]["wiresharkPath"]:
                wiresharkPath = 'wireshark'

            sudo = ''
            if self.CheckBox_sudo.isChecked():
                sudo = 'sudo -S'

            cmd = '{} -{} {}@{} -P {} -pw {} "{} tcpdump -i {} {} -s 0 -l -w -" ' \
                  '| "{}" -k -i -'.format(PlinkFile,
                                          self.protocol,
                                          self.auth["user"],
                                          self.auth["host"],
                                          self.auth["port"],
                                          self.auth["password"],
                                          sudo,
                                          interface,
                                          params,
                                          wiresharkPath
                                          )
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

        if self.kwargs['su']:
            stdin, stdout, stderr = ssh.exec_cmd('su {}'.format(self.kwargs['user_su']))
            out = stdout.read().decode()
            err = stderr.read().decode()
            if 'su' in out:
                stdin, stdout, stderr = ssh.exec_cmd(self.kwargs['password_su'])
                out = stdout.read().decode()
                err = stderr.read().decode()
                if 'Error' in out:
                    self.out_signal.emit(("error", "su 失败：" + out))
                    self.out_signal.emit(("finish", ''))
                    return
                elif 'not found' in out:
                    self.out_signal.emit(("error", "su 失败：" + out))
                    self.out_signal.emit(("finish", ''))
                    return

        stdin, stdout, stderr = ssh.exec_cmd(
            """cat /proc/net/dev | awk '{i++; if(i>2){print $1}}' | sed 's/^[\\t]*//g' | sed 's/[:]*$//g'""")
        # """ls -l /sys/class/net/ | sed '1d' | awk 'BEGIN {FS="/"} {print $NF}'"""

        out = stdout.read().decode()
        err = stderr.read().decode()

        if out:
            self.out_signal.emit(("log", out))
            self.out_signal.emit(("interfaces", out.split('\n')))
            if self.kwargs['su']:
                self.out_signal.emit(
                    ("auth", {"host": self.kwargs['host'], "port": self.kwargs['port'],
                              "user": self.kwargs['user'], "password": self.kwargs['password'],
                              'su': self.kwargs['su'],
                              "user_su": self.kwargs['user_su'], "password_su": self.kwargs['password_su']}))
            else:
                self.out_signal.emit(
                    ("auth", {"host": self.kwargs['host'], "port": self.kwargs['port'],
                              "user": self.kwargs['user'], "password": self.kwargs['password'],
                              'su': self.kwargs['su']}))
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

    # def kill(self, proc_pid):
    #     parent_proc = psutil.Process(proc_pid)
    #     for child_proc in parent_proc.children(recursive=True):
    #         child_proc.kill()
    #     parent_proc.kill()

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


