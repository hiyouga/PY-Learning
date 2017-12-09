@echo off
mode con cols=65 lines=35
title Python interpreter by hiyouga
color 0a
echo Welcome to Python interpreter by hiyouga
echo Now is: %date:~0,10% %time:~0,8%
echo.
cd %cd%
if "%1" == "" (
	color 0c
	echo No input file
	echo Please push down to close the window.
	pause>nul
	exit
)
python %~d1%~p1%~n1%~x1
if %errorlevel% == 1 (
	color 0c
	echo Interpretation error!
)
echo.
echo.
echo Please push down to close the window.
pause>nul