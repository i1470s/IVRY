# /bin/sh
while true
do
rm -rf /home/brayden/desktop/IVRYBot/IVRY-Discord-Bot
git clone git@github.com:i1470s/IVRY-Discord-Bot.git 
echo 
python3 -c 'import sys; print(sys.version_info[:])'
echo
python3 /home/brayden/desktop/IVRYBot/extras/package-updater.py
echo
echo Starting Bot
python3 bot.py
echo Restarting Bot...
done
