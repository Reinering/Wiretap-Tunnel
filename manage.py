# -*- coding: utf-8 -*-
"""
author: Reiner New
email: nbxlhc@hotmail.com
"""

import os
import sys
import platform

# 软件版本信息
APPNAME = "Wiretap Tunnel"
VERSION = "v0.1.00"
PackageTime = ""
RUNTIMEENV = None

# 0: CRITICAL, 1: ERROR, 2: WARNING, 3: INFO, 4: DEBUG
LOGLEVEL = 4

LOGFILE = "logs/app.log"

os_platform = platform.system()
maxbit = sys.maxsize
if maxbit > 2 * 32:
    Computer_Digits = 'x64'
else:
    Computer_Digits = 'x86'

ROOT_PATH = os.getcwd()
PUTTY_PATH = 'PuTTY'

EncodingFormat = 'gbk'

SettingPath = "./data"
SettingFile = "setting.conf"


UI_CONFIG = {
    "theme": "Light",

    "startLogo": "public/images/logo.png",
    "iconPath": ":/images/icons",

    "Material": {
        "AcrylicBlurRadius": 15
    },
    "Update": {
        "CheckUpdateAtStartUp": True
    },
    "Folders": {
        "Download": "",
        "LocalMusic": []
    },
    "MainWindow": {
        "DpiScale": "Auto",
        "Language": "Auto"
    },
    "QFluentWidgets": {
        "ThemeColor": "#ff009faa",
        "ThemeMode": "Dark"
    }
}

if getattr(sys, 'frozen', False):
    BUNDLE_DIR = sys._MEIPASS
    RUNTIMEENV = "pyinstaller"
    PlinkFile = os.path.join(BUNDLE_DIR, PUTTY_PATH, 'plink.exe')
    UI_CONFIG["startLogo"] = os.path.join(BUNDLE_DIR, UI_CONFIG["startLogo"])
else:
    BUNDLE_DIR = os.path.dirname(os.path.abspath(__file__))
    PlinkFile = os.path.join(PUTTY_PATH, 'plink.exe')

SETTINGS = {
    "default": {
        "wiresharkPath": "",
    },
    "linux": {
        "host": [],
        "port": [],
        "user": [],
        "password": [],
        "su_user": [],
        "su_password": [],
        "cmd": []
    },
    "esxi": {
        "host": [],
        "port": [],
        "user": [],
        "password": [],
        "tcpdump": [],
        "pktcap": []
    },
    "tcpdump": [

    ],
    "tcpdump-uw": [

    ],
    "pktcap-uw": {
        "capture": ['Drop', 'Dynamic', 'UplinkRcv', 'UplinkSnd', 'VnicTx', 'VnicRx', 'PortInput',
                    'IOChain', 'EtherswitchDispath', 'EtherswitchOutput', 'PortOutput',
                    'TcpipDispatch', 'PreDVFilter', 'PostDVFilter', 'Drop', 'VdrRxLeaf',
                    'VdrTxLeaf', 'VdrRxTerminal', 'VdrTxTerminal', 'PktFree', 'TcpipRx',
                    'TcpipTx', 'UplinkRcvKernel', 'UplinkSndKernel', 'PreOverlayInput',
                    'PostOverlayInput', 'PreOverlayOutput', 'PostOverlayOutput', 'EnsPortReaderRx',
                    'EnsPortWriterTx', 'EnsPortWriterQueue', 'EnsPortWriterFlush'],
        "outfile": [],
        "count": [],
        "snapLen": [],
        "switchport": [],
        "dir": ['0', 'input', '1', 'output', '2', 'inputAndOutput'],
        "vlan": [],
        "other": []
    }
}