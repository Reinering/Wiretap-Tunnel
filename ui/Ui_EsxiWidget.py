# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EsxiWidget.ui'
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

from .components.combo_box import (MSECComboBox, MSEComboBox)
from qfluentwidgets import (CaptionLabel, ComboBox, EditableComboBox, LineEdit,
    PrimaryPushButton, PushButton, RadioButton)

class Ui_EsxiWidget(object):
    def setupUi(self, EsxiWidget):
        if not EsxiWidget.objectName():
            EsxiWidget.setObjectName(u"EsxiWidget")
        EsxiWidget.resize(560, 564)
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(10)
        EsxiWidget.setFont(font)
        self.gridLayout_4 = QGridLayout(EsxiWidget)
        self.gridLayout_4.setSpacing(3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(1, 5, 1, 1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_ssh = QGroupBox(EsxiWidget)
        self.groupBox_ssh.setObjectName(u"groupBox_ssh")
        self.groupBox_ssh.setMaximumSize(QSize(16777215, 100))
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

        self.PrimaryPushButton_connect = PrimaryPushButton(EsxiWidget)
        self.PrimaryPushButton_connect.setObjectName(u"PrimaryPushButton_connect")
        self.PrimaryPushButton_connect.setFont(font2)

        self.horizontalLayout.addWidget(self.PrimaryPushButton_connect)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_8)


        self.gridLayout_4.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.CaptionLabel_5 = CaptionLabel(EsxiWidget)
        self.CaptionLabel_5.setObjectName(u"CaptionLabel_5")
        self.CaptionLabel_5.setFont(font1)

        self.horizontalLayout_2.addWidget(self.CaptionLabel_5)

        self.ComboBox_interface = ComboBox(EsxiWidget)
        self.ComboBox_interface.setObjectName(u"ComboBox_interface")
        self.ComboBox_interface.setMinimumSize(QSize(200, 33))
        self.ComboBox_interface.setMaximumSize(QSize(16777215, 33))

        self.horizontalLayout_2.addWidget(self.ComboBox_interface)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.gridLayout_4.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBox_cmd = QGroupBox(EsxiWidget)
        self.groupBox_cmd.setObjectName(u"groupBox_cmd")
        self.groupBox_cmd.setMaximumSize(QSize(16777215, 100))
        self.groupBox_cmd.setFont(font1)
        self.gridLayout_3 = QGridLayout(self.groupBox_cmd)
        self.gridLayout_3.setSpacing(3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.RadioButton_tcpdump = RadioButton(self.groupBox_cmd)
        self.RadioButton_tcpdump.setObjectName(u"RadioButton_tcpdump")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setBold(False)
        font3.setItalic(False)
        self.RadioButton_tcpdump.setFont(font3)

        self.verticalLayout_2.addWidget(self.RadioButton_tcpdump)

        self.RadioButton_pktcap = RadioButton(self.groupBox_cmd)
        self.RadioButton_pktcap.setObjectName(u"RadioButton_pktcap")
        self.RadioButton_pktcap.setFont(font3)

        self.verticalLayout_2.addWidget(self.RadioButton_pktcap)


        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.EditableComboBox_tcpdump = EditableComboBox(self.groupBox_cmd)
        self.EditableComboBox_tcpdump.setObjectName(u"EditableComboBox_tcpdump")

        self.verticalLayout_6.addWidget(self.EditableComboBox_tcpdump)

        self.MSECComboBox_pktcap = MSECComboBox(self.groupBox_cmd)
        self.MSECComboBox_pktcap.setObjectName(u"MSECComboBox_pktcap")
        self.MSECComboBox_pktcap.setMinimumSize(QSize(300, 33))

        self.verticalLayout_6.addWidget(self.MSECComboBox_pktcap)


        self.gridLayout_3.addLayout(self.verticalLayout_6, 0, 1, 1, 1)


        self.horizontalLayout_3.addWidget(self.groupBox_cmd)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.PrimaryPushButton_clear = PrimaryPushButton(EsxiWidget)
        self.PrimaryPushButton_clear.setObjectName(u"PrimaryPushButton_clear")
        self.PrimaryPushButton_clear.setFont(font2)

        self.verticalLayout_7.addWidget(self.PrimaryPushButton_clear)

        self.PrimaryPushButton_start = PrimaryPushButton(EsxiWidget)
        self.PrimaryPushButton_start.setObjectName(u"PrimaryPushButton_start")
        self.PrimaryPushButton_start.setFont(font2)

        self.verticalLayout_7.addWidget(self.PrimaryPushButton_start)


        self.horizontalLayout_3.addLayout(self.verticalLayout_7)


        self.gridLayout_4.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        self.groupBox = QGroupBox(EsxiWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setSpacing(3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(3, 3, 3, 3)
        self.textBrowser = QTextBrowser(self.groupBox)
        self.textBrowser.setObjectName(u"textBrowser")

        self.gridLayout_2.addWidget(self.textBrowser, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox, 3, 0, 1, 1)


        self.retranslateUi(EsxiWidget)

        QMetaObject.connectSlotsByName(EsxiWidget)
    # setupUi

    def retranslateUi(self, EsxiWidget):
        EsxiWidget.setWindowTitle(QCoreApplication.translate("EsxiWidget", u"Form", None))
        self.groupBox_ssh.setTitle(QCoreApplication.translate("EsxiWidget", u"SSH", None))
        self.CaptionLabel.setText(QCoreApplication.translate("EsxiWidget", u"Host", None))
        self.CaptionLabel_2.setText(QCoreApplication.translate("EsxiWidget", u"Port", None))
        self.CaptionLabel_3.setText(QCoreApplication.translate("EsxiWidget", u"Username", None))
        self.CaptionLabel_4.setText(QCoreApplication.translate("EsxiWidget", u"Password", None))
        self.PrimaryPushButton_connect.setText(QCoreApplication.translate("EsxiWidget", u"Connect", None))
        self.CaptionLabel_5.setText(QCoreApplication.translate("EsxiWidget", u"Interfaces", None))
        self.groupBox_cmd.setTitle(QCoreApplication.translate("EsxiWidget", u"CMD", None))
        self.RadioButton_tcpdump.setText(QCoreApplication.translate("EsxiWidget", u"tcpdump-uw", None))
        self.RadioButton_pktcap.setText(QCoreApplication.translate("EsxiWidget", u"pktcap-uw", None))
        self.PrimaryPushButton_clear.setText(QCoreApplication.translate("EsxiWidget", u"Clear", None))
        self.PrimaryPushButton_start.setText(QCoreApplication.translate("EsxiWidget", u"Start", None))
        self.groupBox.setTitle(QCoreApplication.translate("EsxiWidget", u"Log", None))
    # retranslateUi

