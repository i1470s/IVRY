import cogs
import random
import discord
import time
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext import commands

client = commands.Bot(command_prefix='.')

class Events(commands.Cog):   
    
        def __init__(self, client):
                self.client = client   

        @commands.Cog.listener()
        async def on_ready(self):
                print("Connecting To The Internet")
                print("Checking DB")
                time.sleep(2)
                print("Loaded Files, The Bot Is Running Normally")
                print("DONE! (Loaded)")

def setup(client):
    client.add_cog(Events(client))