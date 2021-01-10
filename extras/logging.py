import discord
import logging
from logging.handlers import RotatingFileHandler
from cogs import admin, music, general, fun, help, events, xp, nsfw

#LOGGER - DISCORD API

def create_rotating_log(path):

    logger = logging.getLogger('discord')
    logger.setLevel(logging.DEBUG)
    handler = RotatingFileHandler(filename='./data/logs/discord.json', encoding='utf-8', mode='w', maxBytes=937500, backupCount=5)
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)

if __name__ == "discord":
    log_file = "discord.json"
    create_rotating_log(log_file)

#LOGGER - BOT / COGS

def create_rotating_log(path):

    logger2 = logging.getLogger('ivry')
    logger2.setLevel(logging.DEBUG)
    handler = RotatingFileHandler(filename='./data/logs/bot.json', encoding='utf-8', mode='w', maxBytes=937500, backupCount=5)
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger2.addHandler(handler)

if __name__ == "ivry":
    log_file = "bot.json"
    create_rotating_log(log_file)



