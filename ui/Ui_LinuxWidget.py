# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LinuxWidget.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QSizePolicy, QSpacerItem, QTextBrowser, QVBoxLayout,
    QWidget)

from qfluentwidgets import (CaptionLabel, CheckBox, ComboBox, EditableComboBox,
    LineEdit, PrimaryPushButton, PushButton)

class Ui_LinuxWidget(object):
    def setupUi(self, LinuxWidget):
        if not LinuxWidget.objectName():
            LinuxWidget.setObjectName(u"LinuxWidget")
        LinuxWidget.resize(561, 562)
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(10)
        LinuxWidget.setFont(font)
        self.gridLayout_6 = QGridLayout(LinuxWidget)
        self.gridLayout_6.setSpacing(3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(1, 5, 1, 1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_ssh = QGroupBox(LinuxWidget)
        self.groupBox_ssh.setObjectName(u"groupBox_ssh")
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.groupBox_ssh.setFont(font1)
        self.gridLayout = QGridLayout(self.groupBox_ssh)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.CaptionLabel = CaptionLabel(self.groupBox_ssh)
        self.CaptionLabel.setObjectName(u"CaptionLabel")
        font2 = QFont()
        font2.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font2.setPointSize(10)
        font2.setBold(False)
        self.CaptionLabel.setFont(font2)

        self.verticalLayout_3.addWidget(self.CaptionLabel)

        self.CaptionLabel_2 = CaptionLabel(self.groupBox_ssh)
        self.CaptionLabel_2.setObjectName(u"CaptionLabel_2")
        self.CaptionLabel_2.setFont(font2)

        self.verticalLayout_3.addWidget(self.CaptionLabel_2)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.EditableComboBox_host = EditableComboBox(self.groupBox_ssh)
        self.EditableComboBox_host.setObjectName(u"EditableComboBox_host")
        self.EditableComboBox_host.setFont(font2)

        self.verticalLayout_4.addWidget(self.EditableComboBox_host)

        self.EditableComboBox_port = EditableComboBox(self.groupBox_ssh)
        self.EditableComboBox_port.setObjectName(u"EditableComboBox_port")
        self.EditableComboBox_port.setFont(font2)

        self.verticalLayout_4.addWidget(self.EditableComboBox_port)


        self.gridLayout.addLayout(self.verticalLayout_4, 0, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.CaptionLabel_3 = CaptionLabel(self.groupBox_ssh)
        self.CaptionLabel_3.setObjectName(u"CaptionLabel_3")
        self.CaptionLabel_3.setMinimumSize(QSize(70, 0))
        self.CaptionLabel_3.setFont(font2)

        self.verticalLayout.addWidget(self.CaptionLabel_3)

        self.CaptionLabel_4 = CaptionLabel(self.groupBox_ssh)
        self.CaptionLabel_4.setObjectName(u"CaptionLabel_4")
        self.CaptionLabel_4.setFont(font2)

        self.verticalLayout.addWidget(self.CaptionLabel_4)


        self.gridLayout.addLayout(self.verticalLayout, 0, 2, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.EditableComboBox_username = EditableComboBox(self.groupBox_ssh)
        self.EditableComboBox_username.setObjectName(u"EditableComboBox_username")
        self.EditableComboBox_username.setFont(font2)

        self.verticalLayout_5.addWidget(self.EditableComboBox_username)

        self.EditableComboBox_password = EditableComboBox(self.groupBox_ssh)
        self.EditableComboBox_password.setObjectName(u"EditableComboBox_password")
        self.EditableComboBox_password.setFont(font2)

        self.verticalLayout_5.addWidget(self.EditableComboBox_password)


        self.gridLayout.addLayout(self.verticalLayout_5, 0, 3, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox_ssh)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_7)

        self.PrimaryPushButton_connect = PrimaryPushButton(LinuxWidget)
        self.PrimaryPushButton_connect.setObjectName(u"PrimaryPushButton_connect")
        self.PrimaryPushButton_connect.setFont(font2)

        self.horizontalLayout.addWidget(self.PrimaryPushButton_connect)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_8)


        self.gridLayout_6.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.groupBox_privilege = QGroupBox(LinuxWidget)
        self.groupBox_privilege.setObjectName(u"groupBox_privilege")
        self.groupBox_privilege.setFont(font1)
        self.gridLayout_2 = QGridLayout(self.groupBox_privilege)
        self.gridLayout_2.setSpacing(3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.CheckBox_sudo = CheckBox(self.groupBox_privilege)
        self.CheckBox_sudo.setObjectName(u"CheckBox_sudo")
        self.CheckBox_sudo.setMinimumSize(QSize(29, 22))
        self.CheckBox_sudo.setMaximumSize(QSize(65, 16777215))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setBold(False)
        font3.setItalic(False)
        self.CheckBox_sudo.setFont(font3)

        self.horizontalLayout_4.addWidget(self.CheckBox_sudo)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.CheckBox_su = CheckBox(self.groupBox_privilege)
        self.CheckBox_su.setObjectName(u"CheckBox_su")
        self.CheckBox_su.setMinimumSize(QSize(29, 22))
        self.CheckBox_su.setMaximumSize(QSize(45, 16777215))
        self.CheckBox_su.setFont(font3)

        self.horizontalLayout_4.addWidget(self.CheckBox_su)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.CaptionLabel_5 = CaptionLabel(self.groupBox_privilege)
        self.CaptionLabel_5.setObjectName(u"CaptionLabel_5")
        self.CaptionLabel_5.setFont(font2)

        self.horizontalLayout_2.addWidget(self.CaptionLabel_5)

        self.EditableComboBox_su_username = EditableComboBox(self.groupBox_privilege)
        self.EditableComboBox_su_username.setObjectName(u"EditableComboBox_su_username")
        self.EditableComboBox_su_username.setFont(font2)

        self.horizontalLayout_2.addWidget(self.EditableComboBox_su_username)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.CaptionLabel_6 = CaptionLabel(self.groupBox_privilege)
        self.CaptionLabel_6.setObjectName(u"CaptionLabel_6")
        self.CaptionLabel_6.setFont(font2)

        self.horizontalLayout_3.addWidget(self.CaptionLabel_6)

        self.EditableComboBox_su_password = EditableComboBox(self.groupBox_privilege)
        self.EditableComboBox_su_password.setObjectName(u"EditableComboBox_su_password")
        self.EditableComboBox_su_password.setFont(font2)

        self.horizontalLayout_3.addWidget(self.EditableComboBox_su_password)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox_privilege, 1, 0, 1, 1)

        self.groupBox_docker = QGroupBox(LinuxWidget)
        self.groupBox_docker.setObjectName(u"groupBox_docker")
        self.groupBox_docker.setFont(font1)
        self.gridLayout_3 = QGridLayout(self.groupBox_docker)
        self.gridLayout_3.setSpacing(3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.CheckBox_docker = CheckBox(self.groupBox_docker)
        self.CheckBox_docker.setObjectName(u"CheckBox_docker")
        self.CheckBox_docker.setMinimumSize(QSize(29, 22))
        self.CheckBox_docker.setMaximumSize(QSize(70, 16777215))
        self.CheckBox_docker.setFont(font3)

        self.horizontalLayout_7.addWidget(self.CheckBox_docker)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_9)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.CaptionLabel_7 = CaptionLabel(self.groupBox_docker)
        self.CaptionLabel_7.setObjectName(u"CaptionLabel_7")
        self.CaptionLabel_7.setFont(font2)

        self.horizontalLayout_6.addWidget(self.CaptionLabel_7)

        self.EditableComboBox_container = EditableComboBox(self.groupBox_docker)
        self.EditableComboBox_container.setObjectName(u"EditableComboBox_container")
        self.EditableComboBox_container.setFont(font2)

        self.horizontalLayout_6.addWidget(self.EditableComboBox_container)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)


        self.gridLayout_3.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox_docker, 2, 0, 1, 1)

        self.groupBox_interface = QGroupBox(LinuxWidget)
        self.groupBox_interface.setObjectName(u"groupBox_interface")
        self.groupBox_interface.setMinimumSize(QSize(200, 0))
        self.groupBox_interface.setFont(font1)
        self.gridLayout_4 = QGridLayout(self.groupBox_interface)
        self.gridLayout_4.setSpacing(3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(3, 3, 3, 3)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)

        self.CaptionLabel_9 = CaptionLabel(self.groupBox_interface)
        self.CaptionLabel_9.setObjectName(u"CaptionLabel_9")
        self.CaptionLabel_9.setFont(font2)

        self.gridLayout_4.addWidget(self.CaptionLabel_9, 0, 0, 1, 1)

        self.EditableComboBox_cmd = EditableComboBox(self.groupBox_interface)
        self.EditableComboBox_cmd.setObjectName(u"EditableComboBox_cmd")
        self.EditableComboBox_cmd.setMinimumSize(QSize(200, 33))
        self.EditableComboBox_cmd.setFont(font2)

        self.gridLayout_4.addWidget(self.EditableComboBox_cmd, 0, 1, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox_interface, 3, 0, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.CaptionLabel_8 = CaptionLabel(LinuxWidget)
        self.CaptionLabel_8.setObjectName(u"CaptionLabel_8")
        self.CaptionLabel_8.setMaximumSize(QSize(60, 16777215))
        self.CaptionLabel_8.setFont(font2)

        self.horizontalLayout_8.addWidget(self.CaptionLabel_8)

        self.ComboBox_interface = ComboBox(LinuxWidget)
        self.ComboBox_interface.setObjectName(u"ComboBox_interface")
        self.ComboBox_interface.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_8.addWidget(self.ComboBox_interface)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_8)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.PrimaryPushButton_clear = PrimaryPushButton(LinuxWidget)
        self.PrimaryPushButton_clear.setObjectName(u"PrimaryPushButton_clear")

        self.horizontalLayout_9.addWidget(self.PrimaryPushButton_clear)

        self.PrimaryPushButton_start = PrimaryPushButton(LinuxWidget)
        self.PrimaryPushButton_start.setObjectName(u"PrimaryPushButton_start")
        self.PrimaryPushButton_start.setFont(font2)

        self.horizontalLayout_9.addWidget(self.PrimaryPushButton_start)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_9)


        self.gridLayout_6.addLayout(self.horizontalLayout_10, 4, 0, 1, 1)

        self.groupBox = QGroupBox(LinuxWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_5 = QGridLayout(self.groupBox)
        self.gridLayout_5.setSpacing(3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(3, 3, 3, 3)
        self.textBrowser = QTextBrowser(self.groupBox)
        self.textBrowser.setObjectName(u"textBrowser")

        self.gridLayout_5.addWidget(self.textBrowser, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox, 5, 0, 1, 1)


        self.retranslateUi(LinuxWidget)

        QMetaObject.connectSlotsByName(LinuxWidget)
    # setupUi

    def retranslateUi(self, LinuxWidget):
        LinuxWidget.setWindowTitle(QCoreApplication.translate("LinuxWidget", u"Form", None))
        self.groupBox_ssh.setTitle(QCoreApplication.translate("LinuxWidget", u"SSH", None))
        self.CaptionLabel.setText(QCoreApplication.translate("LinuxWidget", u"Host", None))
        self.CaptionLabel_2.setText(QCoreApplication.translate("LinuxWidget", u"Port", None))
        self.CaptionLabel_3.setText(QCoreApplication.translate("LinuxWidget", u"Username", None))
        self.CaptionLabel_4.setText(QCoreApplication.translate("LinuxWidget", u"Password", None))
        self.PrimaryPushButton_connect.setText(QCoreApplication.translate("LinuxWidget", u"Connect", None))
        self.groupBox_privilege.setTitle(QCoreApplication.translate("LinuxWidget", u"Privilege", None))
        self.CheckBox_sudo.setText(QCoreApplication.translate("LinuxWidget", u"sudo", None))
        self.CheckBox_su.setText(QCoreApplication.translate("LinuxWidget", u"su", None))
        self.CaptionLabel_5.setText(QCoreApplication.translate("LinuxWidget", u"Username", None))
        self.CaptionLabel_6.setText(QCoreApplication.translate("LinuxWidget", u"Password", None))
        self.groupBox_docker.setTitle(QCoreApplication.translate("LinuxWidget", u"Docker", None))
        self.CheckBox_docker.setText(QCoreApplication.translate("LinuxWidget", u"docker", None))
        self.CaptionLabel_7.setText(QCoreApplication.translate("LinuxWidget", u"Container name", None))
        self.groupBox_interface.setTitle(QCoreApplication.translate("LinuxWidget", u"Tcpdump", None))
        self.CaptionLabel_9.setText(QCoreApplication.translate("LinuxWidget", u"cmd", None))
        self.CaptionLabel_8.setText(QCoreApplication.translate("LinuxWidget", u"Interfaces", None))
        self.PrimaryPushButton_clear.setText(QCoreApplication.translate("LinuxWidget", u"Clear", None))
        self.PrimaryPushButton_start.setText(QCoreApplication.translate("LinuxWidget", u"Start", None))
        self.groupBox.setTitle(QCoreApplication.translate("LinuxWidget", u"Log", None))
    # retranslateUi

