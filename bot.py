import discord
import logging
import os
from discord.ext import commands
from discord.ext.commands import AutoShardedBot
from asyncio import sleep
from data import config
logger = logging.getLogger("ivry")
logger.debug(f"--------LOADING IVRY {config.version}--------")
logger.debug("bot.py Started")
print(f'''
PUB(BUILD(28))
 _____  ____   ____  _______   ____  ____   
|_   _||_  _| |_  _||_   __ \ |_  _||_  _|  
  | |    \ \   / /    | |__) |  \ \  / /    
  | |     \ \ / /     |  __ /    \ \/ /     
 _| |_     \ ' /     _| |  \ \_  _|  |_     
|_____|     \_/     |____| |___||______| 
----------------------------------------   
| Starting On {config.version}            |‎
| Created By i1470s#0396               |
----------------------------------------
        ~IVRY All Rights Reserved~

--------------ERROR OUTPUT--------------''')

client = commands.AutoShardedBot(command_prefix=config.default_prefix, shard_count=1, case_insensitive=True, intents=discord.Intents.all())
client.remove_command('help')
for ext in os.listdir("./cogs/"):
    if ext.endswith(".py") and not ext.startswith("_"):
        try: client.load_extension(f"cogs.{ext[:-3]}") 
        except Exception as e: 
            print(f'[WARNING] A Fatal internal error occured loading the {ext} cog')
            logger.debug(f"[ERROR] Loading {ext}")

async def status():
    while True:
        await client.wait_until_ready()
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'for {config.default_prefix}Help'))
        await sleep(10)
        await client.change_presence(activity=discord.Game(name=f'on {len(client.guilds)} servers | {config.default_prefix}Help'))
        await sleep(10)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f'{config.shards} | {config.default_prefix}Help'))
        await sleep(10)

#BOT INIT

@client.event
async def on_ready():
    client.loop.create_task(status())
client.run(config.token)