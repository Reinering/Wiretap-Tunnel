@echo off
cls
echo off
echo.
echo ----------------------------��"A"�� ����requirements----------------------------
echo ----------------------------��"I"�� ��װrequirements----------------------------
echo. -----------------------------------by ohxing-----------------------------------
echo.

SET PROJECT_DIR=%~dp0..
SET PYTHON=python
SET FILE=%PROJECT_DIR%\requirements.txt

SET /P Choice=��ѡ�������:
IF /I '%Choice:~0,1%'=='a' GOTO generate
IF /I '%Choice:~0,1%'=='i' GOTO install
IF /I '%Choice:~0,1%'=='q' GOTO quit
exit


:generate
echo ��ʼ����requirements
pipreqs %PROJECT_DIR% --encoding=utf8 --clean %FILE% --force
echo ����requirements�ɹ�

echo. -----------------------------------by ohxing-----------------------------------
echo. ------------------------���в����ɹ�������������˳�---------------------------
pause>nul
exit


:install
%PYTHON% -m pip install -r %file%
echo ��װrequirements�ɹ�

echo. -----------------------------------by ohxing-----------------------------------
echo. ------------------------���в����ɹ�������������˳�---------------------------
pause>nul
exit


:quit
exit