import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')

class Games(commands.Cog):   
    
        def __init__(self, client):
                self.client = client


def setup(client):
    client.add_cog(Games(client))