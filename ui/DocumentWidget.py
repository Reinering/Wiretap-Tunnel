#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module implementing DocumentWidget.
author: Reiner New
email: nbxlc@hotmail.com
"""

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget

from .Ui_DocumentWidget import Ui_DocumentForm


class DocumentWidget(QWidget, Ui_DocumentForm):
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

        self.tabWidget.setCurrentIndex(0)
