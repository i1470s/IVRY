import cogs
import random
import discord
import re
import math
from discord.ext import commands
from data import config

class Help(commands.Cog):   
    
        def __init__(self, client):
                self.client = client        
        

        @commands.command(
            name='help', aliases=['h','commands'], description="Bot commands"
            )
        async def help(self, ctx, cog="1"): 
                helpEmbed = discord.Embed(
                    title='IVRY Commands',
                    description="Prefixes `.` `!` `?` `/` `~` `#` `%` ",
                    color=discord.Color.purple() 
        )
                helpEmbed.set_thumbnail(url=ctx.bot.user.avatar_url)
                helpEmbed.set_footer(text=f"{config.version} | {config.shards}")
                
                cogs = [c for c in self.client.cogs.keys()]  


                totalPages = math.ceil(len(cogs)/6) 

                cog = int(cog)
                if cog > totalPages or cog < 1:
                    await ctx.send(f"Invalid page number: '{cog}'. Please pick from {totalPages} pages.")
                    return

                neededCogs = []
                for i in range(6):
                    x = i + (int(cog) - 1) * 6
                    try:
                        neededCogs.append(cogs[x])
                    except IndexError:
                        pass

                for cog in neededCogs:
                    commandList = ""
                    for command in self.client.get_cog(cog).walk_commands():
                        if command.hidden:
                            continue

                        elif command.parent != None:
                            continue 

                        commandList += f"``{command.name}`` - {command.description}\n"
                    commandList += "\n"
                    
                    helpEmbed.add_field(name=cog, value=commandList, inline=False)

                await ctx.send(embed=helpEmbed)



def setup(client):
    client.add_cog(Help(client))