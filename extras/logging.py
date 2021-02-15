import discord
import logging
from logging.handlers import RotatingFileHandler

#LOGGER - DISCORD API

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = RotatingFileHandler(filename='./data/logs/discord.json', encoding='utf-8', mode='w+', maxBytes=2097152, backupCount=1)
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

#LOGGER - BOT / COGS

logger2 = logging.getLogger('ivry')
logger2.setLevel(logging.DEBUG)
handler = RotatingFileHandler(filename='./data/logs/bot.json', encoding='utf-8', mode='w+', maxBytes=2097152, backupCount=1)
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger2.addHandler(handler)