#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
author: Reiner New
email: nbxlc@hotmail.com
"""


import os
import datetime
from common import pyinstaller
from common import nuitka


Version = "v0.1.00"

now = datetime.datetime.now().strftime("%Y%m%d%H%M")



def overrideSetting(file, typeNum):
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        with open(file, 'w', encoding='utf-8', buffering=1) as f_w:
            for line in lines:
                if "version: " in line:
                    line = "version: " + Version + '\r'
                elif "VERSION = " in line:
                    line = "VERSION = \"" + Version + '\"\r'
                elif "PackageTime = " in line:
                    line = "PackageTime = \"" + now + '\"\r'
                elif "LOGLEVEL = " in line:
                    if typeNum <= 2:
                        line = "LOGLEVEL = 4" + '\r'
                    else:
                        line = "LOGLEVEL = 2" + '\r'
                elif "CURRENT_DB = " in line:
                    if typeNum < 4:
                        line = "CURRENT_DB = \"test\"" + '\r'
                    else:
                        line = "CURRENT_DB = \"deploy\"" + '\r'
                else:
                    pass
                f_w.write(line)
            f.flush()


def pyinstallerPack():
    package = pyinstaller.Package()

    # package.projectFolder = '..\\'
    package.now = now
    package.mainFile = 'main.py'
    package.packageArgs['outName'] = 'Wiretap-Tunnel'

    package.packageArgs['isClean'] = True
    package.packageArgs['hiddenImport'] = [

    ]
    package.packageArgs['addData'] = [
        # windows以;分割，linux以:分割
        # "default:default",
        # "pic;pic",
        # "ui/style;ui/style"
        "public/images;public/images",
        "PuTTY;PuTTY"
    ]
    package.packageArgs['iconPath'] = r'public\icons\favicon.ico'  # 设置打包后的exe图标

    # 输出路径
    # package.packageArgs['distpath'] = r'F:\PythonAPP_Package\Wiretap-Tunnel'

    package.typeNum = 4
    overrideSetting(os.path.join(package.projectFolder, 'manage.py'), package.typeNum)
    package.run()

    # 开启console
    package.typeNum = 2
    overrideSetting(os.path.join(package.projectFolder, 'manage.py'), package.typeNum)
    package.run()


def nuitkaPack():
    package = nuitka.Package()

    # 修改缓存路径：设置环境变量 NUITKA_CACHE_DIR, 否则会在用户缓存目录下生成缓存文件

    # package.projectFolder = '..\\'
    package.now = now
    package.mainFile = 'main.py'
    package.packageArgs['output-filename'] = 'Wiretap-Tunnel'

    package.packageArgs['standalone'] = True
    package.packageArgs['onefile'] = True
    package.packageArgs['windows-icon-from-ico'] = r'public\icons\favicon.ico'  # 设置打包后的exe图标

    # 添加需要打包的资源文件
    package.packageArgs['include-data-files'] = [
        # "file1=file1",
        # "file2=file2"
    ]
    package.packageArgs['include-data-dir'] = [
        "public/images=public/images",
        "PuTTY=PuTTY"
    ]

    # 输出路径
    # package.packageArgs['output-dir'] = r'F:\PythonAPP_Package\Wiretap-Tunnel'

    package.packageArgs['enable-plugin'] = 'pyside6'
    package.packageArgs['lto'] = 'yes'          # 启用LTO优化
    # package.packageArgs['remove-output'] = True     # 编译完成后，自动删除中间文件

    package.typeNum = 4
    overrideSetting(os.path.join(package.projectFolder, 'manage.py'), package.typeNum)
    package.run()

    # 开启console
    package.typeNum = 2
    overrideSetting(os.path.join(package.projectFolder, 'manage.py'), package.typeNum)
    package.run()






if __name__ == '__main__':
    # pyinstallerPack()
    nuitkaPack()