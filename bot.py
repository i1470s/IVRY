import discord
import discord, json
from discord.ext import commands
from discord.ext.commands import AutoShardedBot
import asyncio
from asyncio import sleep
import json
import data 
from data import config

#WORK ON THE GAMES WITH ECHO THEN UPLOAD V.1.5!

client = commands.AutoShardedBot(command_prefix=[".", "!", "?", "/", "~", "#", "%"], shard_count=1, case_insensitive=True)

client.remove_command('help')
client.load_extension("lib.cogs.general")
client.load_extension("lib.cogs.fun")
client.load_extension("lib.cogs.nsfw")
client.load_extension("lib.cogs.music")
client.load_extension("lib.cogs.admin")
client.load_extension("lib.cogs.help")
client.load_extension("lib.cogs.events")

async def status():
    while True:
        await client.wait_until_ready()
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='for .Help'))
        await sleep(10)
        await client.change_presence(activity=discord.Game(name=f'on {len(client.guilds)} servers | .Help'))
        await sleep(10)
@client.event
async def on_ready():
    print(f'{client.user} has Awoken!')
client.loop.create_task(status())

client.run(config.token)
