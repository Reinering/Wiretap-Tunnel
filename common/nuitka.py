#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
author: Reiner New
email: nbxlc@hotmail.com
"""


import subprocess
import datetime
import platform
import os
import sys
from pathlib import Path
import re


os_ver = platform.win32_ver()
print("操作系统：", os_ver)

# maxbit = sys.maxsize
maxbit = int(platform.architecture()[0][:-3])
print("计算机位数：", maxbit)
if maxbit >= 2 * 32:
    Computer_Digits = 'x64'
else:
    Computer_Digits = 'x86'

Type = {
    1: 'Alpha',
    2: 'Beta',
    3: 'RC',
    4: 'Release'
}

"""
修改缓存路径：设置环境变量 NUITKA_CACHE_DIR
"""


class Package:

    def __init__(self):
        self.cacheDir = ''
        self.projectFolder = os.getcwd()
        self.computer_digits = Computer_Digits
        self.typeNum = 2
        self.mainFile = "main.py"
        self.cacheOutPath = 'dist'

        self.now = datetime.datetime.now().strftime("%Y%m%d%H%M")

        self.packageArgs = {
            'module': '',  # 创建一个可导入的二进制扩展模块，而不是程序。默认关闭
            'standalone': False,  # [True, False] 启用独立模式输出。这允许您将创建的二进制文件传输到其他机器上，而无需使用现有的Python安装。这也意味着它会变大。它隐含了"--follow-imports"和"--python-flag=no_site"选项。默认关闭。
            'onefile': False,  # [True, False] 在独立模式的基础上，启用单文件模式。这意味着不是创建一个文件夹，而是创建一个压缩的可执行文件。默认关闭。
            'python-flag': '',  # [flag] 使用Python标志。默认使用您运行Nuitka时使用的标志，这强制使用特定模式
            'python-for-scons': '',  # [path] 使用 Python 3.4 编译时，提供用于 Scons 的 Python 二进制文件的路径
            'python-debug': '',  # 是否使用调试版本。默认使用您运行Nuitka时使用的版本，很可能是非调试版本。仅用于调试和测试目的。
            'main': '',  # [path] 如果指定一次，它将取代位置参数，即要编译的文件名
            'include-package': '',  # 默认为空
            'enable-plugin': '',  # PLUGIN_NAME 启用给定的插件。

            # 模块和包的包含控制
            'include-package': '',  # PACKAGE 包含整个包
            'include-module': '',  # MODULE 包含整个模块
            'include-plugin-directory': '',  # MODULE/PACKAGE 也包含在该目录中找到的代码
            'include-plugin-files': '',  # PATTERN 包含匹配PATTERN的文件。
            'prefer-source-code': '',  # 对于已编译的扩展模块，如果同时存在源文件和扩展模块，通常使用扩展模块，但从可用源代码编译模块可能会获得更好的性能。

            # 导入模块的跟踪控制
            'follow-imports': '',  # 递归到所有导入的模块中。
            'follow-import-to': '',  # MODULE/PACKAGE 如果使用，跟踪到该模块，或如果是包，则跟踪到整个包。
            'nofollow-import-to': '',  # MODULE/PACKAGE 即使使用，也不要跟踪到该模块名称，或如果是包名称，则在任何情况下都不要跟踪到整个包。
            'nofollow-imports': '',  # 完全不递归到任何导入的模块中
            'follow-stdlib': '',  # 也递归到标准库中导入的模块
            'onefile-tempdir-spec': '',  # ONEFILE_TEMPDIR_SPEC 在单文件模式下使用此文件夹进行解包。
            'onefile-child-grace-time': '',  # GRACE_TIME_MS 当停止子进程时，例如由于CTRL-C或关机等，Python代码会收到"KeyboardInterrupt"，可以处理它以刷新数据。这是在以硬方式杀死子进程之前的时间量（毫秒）。
            'onefile-no-compression': '',  # 创建单文件时，禁用有效负载的压缩。
            'onefile-as-archive': '',  # 创建单文件时，使用可以用"nuitka-onefile-unpack"解包的归档格式

            # 数据文件
            'include-package-data': '',  # PACKAGE 包含给定包名称的数据文件
            'include-data-files': '',  # DESC 通过文件名在分发中包含数据文件
            'include-data-dir': '',  # DIRECTORY 在分发中包含完整目录的数据文件。
            'noinclude-data-files': '',  # PATTERN 不包含匹配给定文件名模式的数据文件。
            'include-onefile-external-data': '',  # PATTERN 在单文件二进制文件外部包含指定的数据文件模式
            'list-package-data=LIST_PACKAGE_DATA': '',  # 输出为给定包名称找到的数据文件。
            'include-raw-dir': '',  # DIRECTORY 在分发中完全包含原始目录。

            # 元数据支持
            'include-distribution-metadata': '',  # DISTRIBUTION 包含给定分发名称的元数据信息

            # DLL文件
            'noinclude-dlls': '',  # PATTERN 不包含匹配给定文件名模式的DLL文件。
            'list-package-dlls=LIST_PACKAGE_DLLS': '',  # 输出为给定包名称找到的DLL。

            # 警告控制
            'warn-implicit-exceptions': '',  # 启用对编译时检测到的隐式异常的警告。
            'warn-unusual-code': '',  # 启用对编译时检测到的异常代码的警告。
            'assume-yes-for-downloads': '',  # 允许Nuitka在必要时下载外部代码。
            'nowarn-mnemonic': '',  # MNEMONIC 禁用给定助记符的警告。

            # 编译后立即执行
            'run': False,  # [True, False] 立即执行创建的二进制文件（或导入编译的模块）
            'debugger': '',  # [gdb, lldb, pdb] 使用给定的调试器启动二进制文件, 以自动获取堆栈跟踪。

            # 编译选择
            'user-package-configuration-file': '',  # YAML_FILENAME 用户提供的包配置Yaml文件。
            'full-compat': '',  # 强制与CPython完全兼容
            'file-reference-choice': '',  # MODE 选择"file"将使用的值。
            'module-name-choice': '',  # MODE 选择"name"和"package"将使用的值
            'output-filename': '',  # FILENAME 指定可执行文件应如何命名
            'output-dir': '',  # DIRECTORY 指定中间和最终输出文件应放置的位置。
            'remove-output': '',  # 在生成模块或exe文件后删除构建目录。
            'no-pyi-file': '',  # 不为Nuitka创建的扩展模块创建'.pyi'文件。

            # 部署控制
            'deployment': '',  # 禁用旨在使发现兼容性问题更容易的代码
            'no-deployment-flag': '',  # FLAG 保持部署模式，但选择性地禁用其部分。

            # 环境控制
            'force-runtime-environment-variable': '',  # VARIABLE_SPEC 强制将环境变量设置为给定值。

            # 调试功能
            'debug': '',  # 执行所有可能的自检以查找Nuitka中的错误，不要用于生产。
            'unstripped': '',  # 在结果对象文件中保留调试信息，以便更好地与调试器交互。
            'profile': '',  # 启用基于vmprof的时间消耗分析。目前不工作。
            'internal-graph': '',  # 创建优化过程内部的图表，不要用于整个程序，只用于小型测试用例。
            'trace-execution': '',  # 跟踪执行输出，在执行代码行之前输出它。
            'recompile-c-only': '',  # 这不是增量编译，仅用于Nuitka开发。
            'xml': '',  # XML_FILENAME 以XML形式将内部程序结构、优化结果写入给定文件名。
            'experimental': '',  # FLAG 使用声明为"实验性"的功能。
            'low-memory': '',  #  尝试使用更少的内存。
            'create-environment-from-report': '',  # CREATE_ENVIRONMENT_FROM_REPORT 从给定的报告文件创建新的虚拟环境。
            'generate-c-only': '',  # 仅生成C源代码，不编译为二进制或模块。

            # 后端C编译器
            'clang': '',  # 强制使用clang。
            'mingw64': '',  # 在Windows上强制使用MinGW64。
            'msvc': '',  # MSVC_VERSION 在Windows上强制使用特定MSVC版本
            'jobs': '',  # N 指定允许的并行C编译器作业数。
            'lto': '',  # choice 使用链接时优化（MSVC, gcc, clang）。
            'static-libpython': '',  # choice 使用Python的静态链接库。
            'cf-protection': '',  # PROTECTION_MODE 这个选项是gcc特有的。

            # 缓存控制
            'disable-cache=': '',  # DISABLED_CACHES 禁用选定的缓存。
            'clean-cache': '',  # CLEAN_CACHES 在执行之前清理给定的缓存。
            'disable-bytecode-cache': '',  # 不重用模块的依赖分析结果。
            'disable-ccache': '',  # 不尝试使用ccache（gcc, clang等）或clcache（MSVC, clangcl）。
            'disable-dll-dependency-cache': '',  # 禁用依赖性walker缓存。
            'force-dll-dependency-cache-update': '',  # 强制更新依赖性walker缓存。

            # PGO编译
            'pgo': '',  # 启用C级别的配置文件引导优化（PGO）。
            'pgo-args': '',  # PGO_ARGS 在配置文件引导优化的情况下传递的参数。
            'pgo-executable': '',  # PGO_EXECUTABLE 收集配置文件信息时要执行的命令。
            'report': '',  # REPORT_FILENAME 在XML输出文件中报告模块、数据文件、编译、插件等详细信息。
            'report-diffable': '',  # 以可比较的形式报告数据，即没有每次运行都会变化的时间或内存使用值。
            'report-user-provided': '',  # KEY_VALUE 报告来自您的数据。
            'report-template': '',  # REPORT_DESC 通过模板报告。
            'quiet': '',  # 禁用所有信息输出，但显示警告。
            'show-scons': '',  # 以详细信息运行C构建后端Scons。
            'no-progressbar': '',  # 禁用进度条。
            'show-memory': '',  # 提供内存信息和统计。
            'show-modules': '',  # 提供包含的模块和DLL的信息。
            'show-modules-output': '',  # PATH 输出'--show-modules'的位置。
            'verbose': '',  # 输出所采取行动的详细信息，特别是在优化中。
            'verbose-output': '',  # PATH '--verbose'的输出位置。

            # 通用操作系统控制
            'windows-console-mode': '',  # CONSOLE_MODE [force | disable] 选择要使用的控制台模式。
            'force-stdout-spec': '',  # FORCE_STDOUT_SPEC 强制程序的标准输出到此位置。
            'force-stderr-spec': '',  # FORCE_STDERR_SPEC 强制程序的标准错误到此位置。

            # windows
            'windows-icon-from-ico': '',  # ICON_PATH 指定window 应用程序图标 ico/png 文件
            'windows-icon-template-exe': '',  # ICON_EXE_PATH 指定window 应用程序图标 ico/png 文件
            'onefile-windows-splash-screen-image': '',  # SPLASH_SCREEN_IMAGE 为Windows和单文件模式编译时，在加载应用程序时显示此图像。
            'windows-uac-admin': '',  # 请求Windows用户控制，以在执行时授予管理员权限
            'windows-uac-uiaccess': '',  # 请求Windows用户控制，以强制仅从少数文件夹运行，远程桌面访问。

            # macOS特定控制
            'macos-create-app-bundle': False,  # [True, False] 为macOS编译时，创建一个bundle而不是普通的二进制应用程序。
            'macos-target-arch': '',  # MACOS_TARGET_ARCH: 这应该在哪些架构上运行。
            'macos-app-icon': '',  # ICON_PATH 为应用程序bundle添加图标。
            'macos-signed-app-name': '',  # MACOS_SIGNED_APP_NAME 用于macOS签名的应用程序名称
            'macos-app-name': '',  # MACOS_APP_NAME 在macOS bundle信息中使用的产品名称。
            'macos-app-mode': '',  # MODE 应用程序bundle的应用程序模式。
            'macos-sign-identity': '',  # MACOS_APP_VERSION 在macOS上签名时使用的身份。
            'macos-sign-notarization': '',  # 使用适当的TeamID身份进行公证签名。
            'macos-app-version': '',  # MACOS_APP_VERSION 在macOS bundle信息中使用的产品版本。
            'macos-app-protected-resource': '',  # RESOURCE_DESC 请求访问macOS受保护资源的权限。

            # Linux特定控制
            'enable-plugins': '',  # PLUGIN_NAME 启用的插件。
            'disable-plugins': '',  # PLUGIN_NAME 禁用的插件。
            'user-plugin': '',  # PATH 用户插件的文件名。
            'plugin-list': '',  # 显示所有可用插件的列表并退出
            'plugin-no-detection': '',  # 禁用插件检测机制
            'module-parameter': '',  # MODULE_PARAMETERS 提供模块参数。
            'show-source-changes': '',  # SHOW_SOURCE_CHANGES 显示对原始Python文件内容的源代码更改。
            'noinclude-dask-mode': '',  # NOINCLUDE_DASK_MODE 遇到'dask'导入时的处理方式。
            'noinclude-numba-mode': '',  # NOINCLUDE_NUMBA_MODE 遇到'numba'导入时的处理方式。
            'noinclude-default-mode': '',  # NOINCLUDE_DEFAULT_MODE 为上述选项提供默认的"警告"值。
            'noinclude-custom-mode': '',  # CUSTOM_CHOICES 遇到特定导入时的处理方式。
        }

    def getCMD(self):
        cmd = 'nuitka'
        if self.packageArgs['output-filename']:
            cmd += ' --output-filename=' + self.packageArgs['output-filename']

        if self.packageArgs['output-dir']:
            cmd += ' --output-dir=' + self.packageArgs['output-dir']
        else:
            self.packageArgs['output-dir'] = self.cacheOutPath
            cmd += ' --output-dir=' + self.cacheOutPath

        if self.typeNum == 4:
            cmd += ' --windows-console-mode=' + 'disable'
        elif self.packageArgs['windows-console-mode']:
            cmd += ' --windows-console-mode=' + self.packageArgs['windows-console-mode']

        if self.packageArgs['windows-icon-from-ico']:
            cmd += ' --windows-icon-from-ico=' + self.packageArgs['windows-icon-from-ico']

        if self.packageArgs['module']:
            cmd += ' --module'

        if self.packageArgs['standalone']:
            cmd += ' --standalone'

        if self.packageArgs['onefile']:
            cmd += ' --onefile'

        if self.packageArgs['enable-plugin']:
            cmd += ' --enable-plugin=' + self.packageArgs['enable-plugin']

        if self.packageArgs['include-package']:
            for tmp in self.packageArgs['include-package']:
                cmd += ' --include-package=' + tmp

        if self.packageArgs['include-data-files']:
            for tmp in self.packageArgs['include-data-files']:
                cmd += ' --include-data-files=' + tmp

        if self.packageArgs['include-data-dir']:
            for tmp in self.packageArgs['include-data-dir']:
                cmd += ' --include-data-dir=' + tmp

        if self.packageArgs['lto']:
            cmd += ' --lto=yes'

        if self.packageArgs['remove-output']:
            cmd += ' --remove-output'

        return cmd

    def run(self):
        cmd = self.getCMD()

        cmd = cmd + ' ' + self.mainFile
        cmd = 'cd /d ' + self.projectFolder + ' && ' + cmd
        print(cmd)

        subprocess.run(cmd, shell=True)

        if self.packageArgs['output-filename']:
            if self.typeNum == 4:
                tmp = 'cd /d ' + self.projectFolder + ' && ' + 'move ' + self.packageArgs['output-dir'] + '\\' + self.packageArgs['output-filename'] + '.exe' \
                      + ' ' + self.packageArgs['output-dir'] + '\\"' + self.packageArgs['output-filename'] + '_' + self.computer_digits + '_' + self.now + '.exe"'
            else:
                tmp = 'cd /d ' + self.projectFolder + ' && ' + 'move ' + self.packageArgs['output-dir'] + '\\' + self.packageArgs['output-filename'] + '.exe' \
                      + ' ' + self.packageArgs['output-dir'] + '\\"' + self.packageArgs['output-filename'] + '_' + Type[self.typeNum] + self.computer_digits + '_' + self.now + '.exe"'
        else:
            if self.typeNum == 4:
                tmp = 'cd /d ' + self.projectFolder + ' && ' + 'move ' + self.packageArgs['output-dir'] + '\\' + self.mainFile.replace('.py', '.exe') \
                      + ' ' + self.packageArgs['output-dir'] + '\\"' + self.mainFile.replace('.py', '') + '_' + self.computer_digits + '_' + self.now + '.exe"'
            else:
                tmp = 'cd /d ' + self.projectFolder + ' && ' + 'move ' + self.packageArgs['output-dir'] + '\\' + self.mainFile.replace('.py', '.exe') \
                      + ' ' + self.packageArgs['output-dir'] + '\\"' + self.mainFile.replace('.py', '') + '_' + Type[self.typeNum] + self.computer_digits + '_' + self.now + '.exe"'

        subprocess.run(tmp, shell=True)
