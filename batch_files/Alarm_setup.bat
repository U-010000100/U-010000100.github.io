@echo off
title Alarm Setup
echo Setting Things Up
pip install playsound
mkdir Alarm_audio
move alarm.mp3 ./Alarm_audio/
del Alarm_setup.bat
echo Done!
pause