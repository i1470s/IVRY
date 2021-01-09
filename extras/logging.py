import discord
import logging
from cogs import admin, music, general, fun, help, events, xp, nsfw

#LOGGER - DISCORD API

discord = logging.getLogger('discord')
discord.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='./data/logs/discord.json', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
discord.addHandler(handler)

#FINISH FOR V.3.0

#LOGGER - BOT

bot = logging.getLogger('bot')
bot.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='./data/logs/bot.json', encoding='utf-8', mode='w')
bot.addHandler(handler)
