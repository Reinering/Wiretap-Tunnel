#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module implementing MainWindow.
author: Reiner New
email: nbxlc@hotmail.com
"""
import os
from PySide6.QtCore import Slot, Qt, QCoreApplication, QMetaObject
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QGridLayout

from .utils.icon import AppIcon

from .Ui_MainWindow import Ui_Form
from .LinuxWidget import LinuxWidget
from .EsxiWidget import EsxiWidget
from .SettingsWidget import SettingsWidget
from .DocumentWidget import DocumentWidget
from qframelesswindow import FramelessWindow, StandardTitleBar
from qfluentwidgets import NavigationItemPosition

from manage import APPNAME, UI_CONFIG, RUNTIMEENV, BUNDLE_DIR, PUTTY_PATH


class MainWindow(FramelessWindow, Ui_Form):
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
        QMetaObject.connectSlotsByName(self)
        self.translate = QCoreApplication.translate
        self.subInterfaceList = []

        self.initTitleBar()

        self.initNavi()

        self.initWidget()

        if RUNTIMEENV == "pyinstaller":
            self.plinkFile = os.path.join(BUNDLE_DIR, PUTTY_PATH, 'plink.exe')
        else:
            self.plinkFile = os.path.join(PUTTY_PATH, 'plink.exe')

        self.isVisible()

    def initWidget(self):
        # set window icon
        self.setWindowIcon(QIcon(':/logo/images/logo.png'))

        # title setting

        #
        self.gridLayout_main = QGridLayout(self.mainframe)
        self.gridLayout_main.setSpacing(3)
        self.gridLayout_main.setObjectName(u"gridLayout_main")
        self.gridLayout_main.setContentsMargins(1, 1, 1, 1)

        # create sub interface
        self.linux = LinuxWidget(self)
        self.subInterfaceList.append(self.linux)
        self.gridLayout_main.addWidget(self.linux)
        self.linux.hide()
        self.esxi = EsxiWidget(self)
        self.subInterfaceList.append(self.esxi)
        self.gridLayout_main.addWidget(self.esxi)
        self.esxi.hide()
        self.settings = SettingsWidget(self)
        self.subInterfaceList.append(self.settings)
        self.gridLayout_main.addWidget(self.settings)
        self.settings.hide()
        self.document = DocumentWidget(self)
        self.subInterfaceList.append(self.document)
        self.gridLayout_main.addWidget(self.document)
        self.document.hide()



    def initTitleBar(self):
        self.setTitleBar(StandardTitleBar(self))
        # self.setTitleBar(CustomTitleBar(self))
        self.setWindowTitle(APPNAME)
        self.titleBar.setAttribute(Qt.WA_StyledBackground)

    # add items to navigation interface
    def initNavi(self):
        # navigator setting
        # self.NavigationInterface.setProperty("showMenu", True)
        # self.NavigationInterface.setProperty("showReturn", True)
        # 导航栏与主界面同高，展开后不覆盖标题栏
        self.NavigationInterface.displayModeChanged.connect(self.titleBar.raise_)
        self.titleBar.raise_()
        # 展开宽度
        self.NavigationInterface.panel.setExpandWidth(150)

        # 设置 导航栏的偏移
        self.gridLayout.setSpacing(0)
        self.gridLayout.setContentsMargins(3, self.titleBar.height(), 3, 3)

        # create sub interface

        # add navigation items
        self.NavigationInterface.addItem(
            routeKey="home",
            # icon=QIcon(f":/images/icons/light/home.svg"),
            icon=AppIcon.HOME.icon(UI_CONFIG["theme"].lower()),
            text="Home",
            # onClick=lambda t: self.switchTo(self.linux, t),
            position=NavigationItemPosition.SCROLL,
            tooltip="Home"
        )
        self.NavigationInterface.addItem(
            routeKey="linux",
            icon=AppIcon.LINUX.icon(UI_CONFIG["theme"].lower()),
            text="Linux",
            onClick=lambda t: self.switchTo(self.linux, t),
            position=NavigationItemPosition.SCROLL,
            tooltip="Linux"
        )
        self.NavigationInterface.addItem(
            routeKey="esxi",
            icon=AppIcon.ESXI.icon(UI_CONFIG["theme"].lower()),
            text="Esxi",
            onClick=lambda t: self.switchTo(self.esxi, t),
            position=NavigationItemPosition.SCROLL,
            tooltip="VM Esxi"
        )
        self.NavigationInterface.addItem(
            routeKey="settings",
            icon=AppIcon.SETTINGS.icon(UI_CONFIG["theme"].lower()),
            text="Settings",
            onClick=lambda t: self.switchTo(self.settings, t),
            position=NavigationItemPosition.SCROLL,
            tooltip="Settings"
        )
        self.NavigationInterface.addItem(
            routeKey="documents",
            icon=AppIcon.DOCUMENT.icon(UI_CONFIG["theme"].lower()),
            text="Ducuments",
            onClick=lambda t: self.switchTo(self.document, t),
            position=NavigationItemPosition.SCROLL,
            tooltip="Documents"
        )

    #
    def resizeEvent(self, e):
        self.titleBar.move(46, 0)
        self.titleBar.resize(self.width() - 46, self.titleBar.height())

    def switchTo(self, widget, triggerByUser=True):
        for sub in self.subInterfaceList:
            if sub.isHidden() == False:
                sub.hide()

        widget.show()

    def closeEvent(self, *args, **kwargs):
        print("close")