import cogs
import random
import discord
from discord.ext import commands
import sys

client = commands.Bot(command_prefix='.')

class Admin_Commands(commands.Cog):   
    
        def __init__(self, client,):
                self.client = client 

        @commands.command(name='ban', description="Ban members")
        @commands.has_permissions(ban_members = True)
        async def ban(self,ctx,member : discord.Member,*,reason="No reason provided"):
                await ctx.send(member.name+ " has been banned from the server!")
                await member.ban(reason=reason)

        @commands.command(name='kick', description="Kick members")
        @commands.has_permissions(ban_members = True)
        async def kick(self,ctx,member : discord.Member,*,reason="No reason provided"):
                await ctx.send(member.name+ " has been kicked from the server!")
                await member.kick(reason=reason)

        @commands.command(name='mute', description="Mute members")
        @commands.has_permissions(ban_members = True)
        async def mute(self,ctx,member : discord.Member):
                muted_role = ctx.guild.get_role(761473223140573184)

                await member.add_roles(muted_role) 

                await ctx.send(member.mention + " has been muted") 

        @commands.command(name='unban', description="Unban members")
        @commands.has_permissions(ban_members = True)
        async def unban(self,ctx,*,member):
                banned_users = await ctx.guild.bans()
                member_name, member_disc = member.split('#')

                for banned_entry in banned_users:
                        user = banned_entry.user

                        if (user.name, user.discriminator)==(member_name,member_disc):

                                await ctx.guild.unban(user)
                                await ctx.send(member_name +" has been unbanned")

        @commands.command(name='unmute', description="Unmute members")
        @commands.has_permissions(ban_members = True)
        async def unmute(self,ctx,member : discord.Member):
                muted_role = ctx.guild.get_role(761473223140573184)

                await member.remove_roles(muted_role)

                await ctx.send(member.mention + " has been unmuted")
        
        @commands.command(name='restart', description="Restart the bot")
        @commands.is_owner()
        async def restart(self, ctx):  
                await ctx.send(f'Restarting...')
                sys.exit()

def setup(client):
    client.add_cog(Admin_Commands(client))