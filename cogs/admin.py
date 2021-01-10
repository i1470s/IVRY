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

bot = logging.getLogger(__name__)

class Admin(commands.Cog):   
    
        def __init__(self, client,):
                self.client = client 

        #BAN

        @commands.command(name='ban', description="Ban members")
        @commands.guild_only()
        @commands.has_permissions(ban_members = True)
        async def ban(self,ctx,member : discord.Member,*,reason="No reason provided"):
                await ctx.send(member.name+ " has been banned from the server!")
                await member.ban(reason=reason)

        #KICK

        @commands.command(name='kick', description="Kick members")
        @commands.guild_only()
        @commands.has_permissions(kick_members = True)
        async def kick(self,ctx,member : discord.Member,*,reason="No reason provided"):
                await ctx.send(member.name+ " has been kicked from the server!")
                await member.kick(reason=reason)

        #MUTE

        @commands.command(name='mute', description="Mute members")
        @commands.guild_only()
        @commands.has_permissions(manage_guild = True)
        async def mute(self,ctx,member : discord.Member):
                muted_role = discord.utils.get(ctx.guild.roles, name="Muted")

                await member.add_roles(muted_role) 
                
                await ctx.send(member.mention + " has been muted") 

        #UNBAN

        @commands.command(name='unban', description="Unban members")
        @commands.guild_only()
        @commands.has_permissions(ban_members = True)
        async def unban(self,ctx,*,member):
                banned_users = await ctx.guild.bans()
                member_name, member_disc = member.split('#')

                for banned_entry in banned_users:
                        user = banned_entry.user

                        if (user.name, user.discriminator)==(member_name,member_disc):

                                await ctx.guild.unban(user)
                                await ctx.send(member_name +" has been unbanned")

        #UNMUTE

        @commands.command(name='unmute', description="Unmute members")
        @commands.guild_only()
        @commands.has_permissions(manage_guild = True)
        async def unmute(self,ctx,member : discord.Member):
                muted_role = discord.utils.get(ctx.guild.roles, name="Muted")

                await member.remove_roles(muted_role)

                await ctx.send(member.mention + " has been unmuted")

        #PURGE

        @commands.command(name='clear', description="Delete messages")
        @commands.guild_only()
        @commands.has_permissions(manage_guild = True)
        async def clear(self, ctx, ammount=100):
                await ctx.channel.purge(limit=ammount)

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
    client.add_cog(Admin(client))