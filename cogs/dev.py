import random
import discord
from discord.ext import commands
import sys
import traceback
import os
import asyncio
from asyncio import sleep
import math
from data import config, wordlist
import logging
logger3 = logging.getLogger("ivry")
logger3.debug("dev.py Started")

class Dev(commands.Cog):   
    
        def __init__(self, client,):
                self.client = client 

        #RESTART

        @commands.command(hidden=True)
        @commands.is_owner()
        async def restart(self, ctx):  
                await ctx.send(f'Restarting...')
                sys.exit()

        #RELOAD 

        @commands.command(hidden=True)
        @commands.is_owner()
        async def reload(self, ctx, cog=None):
                if not cog:
                        async with ctx.typing():
                                embed = discord.Embed(
                                        title="Reloaded cogs",
                                        color=0x9B59B6,
                                        timestamp=ctx.message.created_at
                                )
                                for ext in os.listdir("./cogs/"):
                                        if ext.endswith(".py") and not ext.startswith("_"):
                                                try:
                                                        self.client.unload_extension(f"cogs.{ext[:-3]}")
                                                        self.client.load_extension(f"cogs.{ext[:-3]}")
                                                        embed.add_field(
                                                                name=f"Reloaded: `{ext}`",
                                                                value='\uFEFF',
                                                                inline=False
                                                        )
                                                except Exception as e:
                                                        embed.add_field(
                                                                name=f"Failed to reload `{ext}`",
                                                                value=e,
                                                                inline=False
                                                        )
                                        await asyncio.sleep(0.5)
                                await ctx.send(embed=embed)
                else:
                        async with ctx.typing():
                                embed = discord.Embed(
                                        title="Reloading all cogs",
                                        color=0x9B59B6,
                                        timestamp=ctx.message.created_at
                                )
                                ext = f"{cog.lower()}.py"
                                if not os.path.exists(f"./cogs/{ext}"):
                                        embed.add_field(
                                                name=f"Failed to reload: {ext}",
                                                value="This cog does not exist.",
                                                inline=False
                                        )
                                
                                elif ext.endswith(".py") and not ext.startswith("_"):
                                        try:
                                                self.client.unload_extension(f"cogs.{ext[:-3]}")
                                                self.client.load_extension(f"cogs.{ext[:-3]}")
                                                embed.add_field(
                                                        name=f"Reloaded: `{ext}`",
                                                        value='\uFEFF',
                                                        inline=False
                                                )
                                        except Exception:
                                                desired_trace = traceback.format_exc()
                                                embed.add_field(
                                                        name=f"Failed to reload: `{ext}`",
                                                        value=desired_trace
                                                )
                                await ctx.send(embed=embed)

        #EVAL

        @commands.command()
        @commands.is_owner()
        async def eval(self, ctx, *, cmd=None):
                try:
                        eval(cmd)
                        await ctx.send(f'Command exectued succsessfuly --> `{cmd}`')
                except:
                        print(f'`{cmd}` is an invalid command')
                        await ctx.send(f'Could not execute an invalid command --> `{cmd}`')

        #LEAVE SERVER

        @commands.command(hidden=True)
        @commands.is_owner()
        async def leaveserver(self, ctx, guildid: str):
                if guildid == 'this':
                        await ctx.guild.leave()
                
                else:
                        guild = self.client.get_guild(guildid)
                if guild:
                        await guild.leave()
                        msg = f':ok: I have left the {guild.name} server!'
                else:
                        msg = ':x: Could not find that server id!'
                await ctx.send(msg)

        #LOGS

        @commands.group(invoke_without_command=True)
        @commands.is_owner()
        async def logs(self, ctx):
                embed = discord.Embed(color=0x9B59B6)

                embed.set_author(name="IVRY Log", icon_url=self.client.user.avatar_url)
                embed.add_field(name = "Avalible Logs", value=f"\n `bot`- Bot errors / data logs \n `discord`- Discord API logs \n `xp`- User xp database \n `settings`- Guild Settings Database", inline=True)
                embed.set_footer(text=f"{config.version} | {config.shards}")
                        
                await ctx.send(embed=embed)

        #BOT SUB COMMAND

        @logs.command()
        async def bot(self, ctx):
                await ctx.send(file=discord.File(r'./data/logs/bot.json'))

        #DISCORD SUB COMMAND

        @logs.command()
        async def discord(self, ctx):
                await ctx.send(file=discord.File(r'./data/logs/discord.json'))

        #XP SUB COMMAND

        @logs.command()
        async def xp(self, ctx):
                await ctx.send(file=discord.File(r'./data/dbs/users-xp.json'))

        #SETTINGS SUB COMMAND

        @logs.command()
        async def settings(self, ctx):
                await ctx.send(file=discord.File(r'./data/dbs/guild-settings.json'))

        #ANTI SWEAR AND FILE    

        @commands.Cog.listener()
        @commands.guild_only()
        async def on_message(self, message):
                word_list = (wordlist.words)

                if message.author == self.client.user:
                        return

                messageContent = message.content
                if len(messageContent) > 0:
                        for word in word_list:
                                if word in messageContent:
                                        await message.delete()
                                        await message.channel.send(f'`{message.content}` Is in our banned words list, Please refrain from using it!')
                        
                messageattachments = message.attachments
                if len(messageattachments) > 0:
                        for attachment in messageattachments:
                                if attachment.filename.endswith(".dll"):
                                        await message.delete()
                                        await message.channel.send("This file type is not allowed in this server.")
                        else: 
                                return

def setup(client):
    client.add_cog(Dev(client))