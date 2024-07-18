#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
author: Reiner New
email: nbxlc@hotmail.com
"""


from enum import Enum

from qfluentwidgets import getIconColor, Theme, FluentIconBase

from manage import UI_CONFIG


class AppIcon(FluentIconBase, Enum):

    HOME = "home"
    LINUX = "linux"
    ESXI = "esxi"
    SETTINGS = "settings"
    DOCUMENT = "document"
    LOG = "log"

    def path(self, theme=Theme.AUTO):
        return f"{UI_CONFIG['iconPath']}/{theme}/{self.value}.svg"