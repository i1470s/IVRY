#PRIMARY IMPORTS

import discord, logging

#SECONDARY IMPORTS

from logging.handlers import RotatingFileHandler

#LOGGER - DISCORD API

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = RotatingFileHandler(filename='./data/logs/discord.json', encoding='utf-8', mode='w+', maxBytes=7340032, backupCount=1)
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

#LOGGER - BOT / COGS

logger = logging.getLogger('ivry')
logger.setLevel(logging.DEBUG)
handler = RotatingFileHandler(filename='./data/logs/bot.json', encoding='utf-8', mode='w+', maxBytes=7340032, backupCount=1)
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)