import discord
import logging
from cogs import admin, music, general, fun, help, events, xp, nsfw

#LOGGER - DISCORD API

logger2 = logging.getLogger('discord')
logger2.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='./data/logs/discord.json', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger2.addHandler(handler)

#LOGGER - BOT / COGS

logger3 = logging.getLogger('ivry')
logger3.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='./data/logs/bot.json', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger3.addHandler(handler)





