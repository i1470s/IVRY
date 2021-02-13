# /bin/sh
while true
do
echo
echo ---PYTHON VERSION---
echo
python3 -c 'import sys; print(sys.version_info[:])'
echo
echo ---REPO UPDATER---
echo
rm -rf /home/brayden/desktop/IVRYBot/IVRY-Discord-Bot
git clone git@github.com:i1470s/IVRY-Discord-Bot.git 
echo
echo ---PACKAGE UPDATER---
echo
python3 /home/brayden/desktop/IVRYBot/extras/package-updater.py
echo
echo ---BOT INIT---
echo
python3 bot.py
done
