import random
import discord
from discord.ext import commands
import sys
import traceback
import os
import asyncio
from asyncio import sleep
import math
from data import config
import logging
logger3 = logging.getLogger("ivry")
logger3.debug("admin.py Started")

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

def setup(client):
    client.add_cog(Admin(client))