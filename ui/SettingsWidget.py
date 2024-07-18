#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module implementing SettingsWidget.
author: Reiner New
email: nbxlc@hotmail.com
"""

from PySide6.QtCore import Slot, QCoreApplication
from PySide6.QtWidgets import QWidget, QFileDialog

from .Ui_SettingsWidget import Ui_SettingsWidget
from .components.tip import Tip
from common.wintools import findProgramPath
from qfluentwidgets import TeachingTip, InfoBarIcon, TeachingTipTailPosition
from .utils.config import saveConfig
from manage import SETTINGS


class SettingsWidget(QWidget, Ui_SettingsWidget):
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

        self.initWidget()
        self.count = 0

    def initWidget(self):
        # init setting
        wiresharkPath = findProgramPath("wireshark.exe")
        if wiresharkPath:
            SETTINGS["default"]["wiresharkPath"] = wiresharkPath
            saveConfig()
        self.LineEdit_wiresharkPath.setText(SETTINGS["default"]["wiresharkPath"])

    @Slot()
    def on_PrimaryPushButton_select_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        try:
            filePath = QFileDialog.getOpenFileName(self, u"选择文件", "/",
                                                   "wireshark(wireshark.exe)")
            if not filePath[0]:
                return

            self.LineEdit_wiresharkPath.setText(filePath[0])
            SETTINGS["default"]["wiresharkPath"] = filePath[0]
        except Exception as e:
            print(e)

    @Slot()
    def on_PrimaryPushButton_save_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        saveConfig()

        Tip.success(self, self.PrimaryPushButton_save, "保存完成")


