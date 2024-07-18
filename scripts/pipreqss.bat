@echo off
cls
echo off
echo.
echo ----------------------------按"A"键 生成requirements----------------------------
echo ----------------------------按"I"键 安装requirements----------------------------
echo. -----------------------------------by ohxing-----------------------------------
echo.

SET PROJECT_DIR=%~dp0..
SET PYTHON=python
SET FILE=%PROJECT_DIR%\requirements.txt

SET /P Choice=请选择操作项:
IF /I '%Choice:~0,1%'=='a' GOTO generate
IF /I '%Choice:~0,1%'=='i' GOTO install
IF /I '%Choice:~0,1%'=='q' GOTO quit
exit


:generate
echo 开始生成requirements
pipreqs %PROJECT_DIR% --encoding=utf8 --clean %FILE% --force
echo 生成requirements成功

echo. -----------------------------------by ohxing-----------------------------------
echo. ------------------------所有操作成功！按任意键可退出---------------------------
pause>nul
exit


:install
%PYTHON% -m pip install -r %file%
echo 安装requirements成功

echo. -----------------------------------by ohxing-----------------------------------
echo. ------------------------所有操作成功！按任意键可退出---------------------------
pause>nul
exit


:quit
exit