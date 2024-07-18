# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QSizePolicy,
    QWidget)

from qfluentexpand.components.navigation.navigation_interface import Navigation
from qfluentwidgets import NavigationInterface
import resource_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(559, 562)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(1, 1, 1, 1)
        self.NavigationInterface = Navigation(Form)
        self.NavigationInterface.setObjectName(u"NavigationInterface")
        font = QFont()
        font.setPointSize(10)
        self.NavigationInterface.setFont(font)

        self.gridLayout.addWidget(self.NavigationInterface, 0, 0, 1, 1)

        self.mainframe = QFrame(Form)
        self.mainframe.setObjectName(u"mainframe")
        self.mainframe.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainframe.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout.addWidget(self.mainframe, 0, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
    # retranslateUi

