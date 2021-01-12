import os
import discord
from discord.ext import commands
from discord.ext.commands import AutoShardedBot
from asyncio import sleep
from extras import logging
from data import config
import logging
logger3 = logging.getLogger("ivry")
logger3.debug(f"--------LOADING IVRY {config.version}--------")
logger3.debug("bot.py Started")

client = commands.AutoShardedBot(command_prefix=config.default_prefix, shard_count=1, case_insensitive=True, intents=discord.Intents.all())
client.remove_command('help')
for ext in os.listdir("./cogs/"):
    if ext.endswith(".py") and not ext.startswith("_"):
        try: client.load_extension(f"cogs.{ext[:-3]}") 
        except Exception as e: 
            print(f'[WARNING] A Fatal internal error occured loading the {ext} cog')
            logger3.debug(f"[ERROR] Loading {ext}")

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