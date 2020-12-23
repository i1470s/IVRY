import discord
from discord.ext import commands
from discord.ext.commands import AutoShardedBot
from asyncio import sleep
from extras import logging
from data import config

intents=discord.Intents.all()
client = commands.AutoShardedBot(command_prefix=config.default_prefix, shard_count=1, case_insensitive=True, intents=intents)

client.remove_command('help')
client.load_extension("cogs.general")
client.load_extension("cogs.fun")
client.load_extension("cogs.nsfw")
client.load_extension("cogs.music")
client.load_extension("cogs.admin")
client.load_extension("cogs.help")
client.load_extension("cogs.xp")
client.load_extension("cogs.events")

async def status():
    while True:
        await client.wait_until_ready()
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'for {config.default_prefix}Help'))
        await sleep(10)
        await client.change_presence(activity=discord.Game(name=f'on {len(client.guilds)} servers | {config.default_prefix}Help'))
        await sleep(10)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f'{config.shards} | {config.default_prefix}Help'))
        await sleep(10)

@client.event
async def on_ready():
    print(f'Starting IVRY on {config.version}')
client.loop.create_task(status())
client.run(config.token)