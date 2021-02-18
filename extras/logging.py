import discord, logging
from logging.handlers import RotatingFileHandler

#LOGGER - DISCORD API

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = RotatingFileHandler(filename='./data/logs/discord.json', encoding='utf-8', mode='w+', maxBytes=2097152, backupCount=1)
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

#LOGGER - BOT / COGS

logger3 = logging.getLogger('ivry')
logger3.setLevel(logging.DEBUG)
handler = RotatingFileHandler(filename='./data/logs/bot.json', encoding='utf-8', mode='w+', maxBytes=2097152, backupCount=1)
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger3.addHandler(handler)