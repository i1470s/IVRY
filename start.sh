# /bin/sh
while true
do
echo
echo ---IVRY INIT - Version - 1.0---
echo
sleep 3
echo Created by i1470s#3096
echo
echo ---PYTHON VERSION---
echo
sleep 5
python3 -c 'import sys; print(sys.version_info[:])'
echo
echo ---REPO UPDATER---
echo
sleep 5
rm -rf /home/brayden/Desktop/IVRYBot/IVRY-Discord-Bot
git clone git@github.com:i1470s/IVRY-Discord-Bot.git 
echo
echo ---PACKAGE UPDATER---
echo
sleep 5
pip3 install -r requirements.txt --upgrade
echo
echo ---BOT INIT---
echo
sleep 5
python3 bot.py
done
