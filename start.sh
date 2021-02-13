# /bin/sh
while true
do
echo  _____  ____   ____  _______   ____  ____   
echo |_   _||_  _| |_  _||_   __ \ |_  _||_  _|  
echo   | |    \ \   / /    | |__) |  \ \  / /    
echo   | |     \ \ / /     |  __ /    \ \/ /     
echo  _| |_     \   /     _| |  \ \_  _|  |_     
echo |_____|     \_/     |____| |___||______|
echo    Created by i1470s#0396 Welcome :)
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
