import logging
import discord
from logging.handlers import RotatingFileHandler

#LOGGER - DISCORD API

logger0 = logging.getLogger('discord')
logger0.setLevel(logging.DEBUG)
handler = RotatingFileHandler(filename='./data/logs/discord.json', encoding='utf-8', mode='w+', maxBytes=2097152, backupCount=1)
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger0.addHandler(handler)

#LOGGER - BOT / COGS

logger = logging.getLogger('ivry')
logger.setLevel(logging.DEBUG)
handler = RotatingFileHandler(filename='./data/logs/bot.json', encoding='utf-8', mode='w+', maxBytes=2097152, backupCount=1)
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)