# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SettingsWidget.ui'
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
    QSizePolicy, QSpacerItem, QWidget)

from qfluentwidgets import (CaptionLabel, LineEdit, PrimaryPushButton, PushButton)

class Ui_SettingsWidget(object):
    def setupUi(self, SettingsWidget):
        if not SettingsWidget.objectName():
            SettingsWidget.setObjectName(u"SettingsWidget")
        SettingsWidget.resize(554, 495)
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(10)
        SettingsWidget.setFont(font)
        self.gridLayout_2 = QGridLayout(SettingsWidget)
        self.gridLayout_2.setSpacing(3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(1, 5, 1, 1)
        self.groupBox = QGroupBox(SettingsWidget)
        self.groupBox.setObjectName(u"groupBox")
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.groupBox.setFont(font1)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(3, 3, 3, 3)
        self.PrimaryPushButton_select = PrimaryPushButton(self.groupBox)
        self.PrimaryPushButton_select.setObjectName(u"PrimaryPushButton_select")
        font2 = QFont()
        font2.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font2.setPointSize(10)
        font2.setBold(False)
        self.PrimaryPushButton_select.setFont(font2)

        self.gridLayout.addWidget(self.PrimaryPushButton_select, 0, 2, 1, 1)

        self.CaptionLabel = CaptionLabel(self.groupBox)
        self.CaptionLabel.setObjectName(u"CaptionLabel")
        self.CaptionLabel.setFont(font2)

        self.gridLayout.addWidget(self.CaptionLabel, 0, 0, 1, 1)

        self.LineEdit_wiresharkPath = LineEdit(self.groupBox)
        self.LineEdit_wiresharkPath.setObjectName(u"LineEdit_wiresharkPath")
        self.LineEdit_wiresharkPath.setFont(font2)

        self.gridLayout.addWidget(self.LineEdit_wiresharkPath, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 376, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.PrimaryPushButton_save = PrimaryPushButton(SettingsWidget)
        self.PrimaryPushButton_save.setObjectName(u"PrimaryPushButton_save")
        self.PrimaryPushButton_save.setFont(font2)

        self.horizontalLayout.addWidget(self.PrimaryPushButton_save)


        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 1)


        self.retranslateUi(SettingsWidget)

        QMetaObject.connectSlotsByName(SettingsWidget)
    # setupUi

    def retranslateUi(self, SettingsWidget):
        SettingsWidget.setWindowTitle(QCoreApplication.translate("SettingsWidget", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("SettingsWidget", u"WireShark", None))
        self.PrimaryPushButton_select.setText(QCoreApplication.translate("SettingsWidget", u"select", None))
        self.CaptionLabel.setText(QCoreApplication.translate("SettingsWidget", u"Path", None))
        self.PrimaryPushButton_save.setText(QCoreApplication.translate("SettingsWidget", u"Save", None))
    # retranslateUi

