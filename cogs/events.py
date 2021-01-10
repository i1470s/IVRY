import random
import os
import discord
import datetime
import sys
import traceback
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext import commands
import json
from data import config
import logging

bot = logging.getLogger(__name__)

class Events(commands.Cog):   
    
        def __init__(self, client):
                self.client = client

        #ON NEW GUILD JOIN

        @commands.Cog.listener()
        async def on_guild_join(self, guild):
                channel = discord.utils.get(guild.text_channels, name="general")
                if channel:
                        embed = discord.Embed(title = f"Prefix {config.prefix}", description=f"Thanks for inviting me :smile::clap:! Im happy to be apart of `{guild.name}` :tada::smile:. Make use {config.prefix}Help for a list of my commands!",color=0x9B59B6,)

                        embed.set_author(name="IVRY Info", icon_url=guild.me.avatar_url)
                        embed.set_thumbnail(url=guild.me.avatar_url)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                        embed.add_field(name = "Additional Resources", value=":video_game: [IVRY Server](https://discord.gg/ppn2u99)\n:iphone: [Website](https://ivry.tk)", inline=False)

                        await channel.send(embed=embed)

        #GUILD MEMBER JOIN

        @commands.Cog.listener()
        async def on_member_join(self, member):
                join_role = discord.utils.get(member.guild.roles, name="Member")
                channel = discord.utils.get(member.guild.text_channels, name="welcome")
                if channel:
                        embed = discord.Embed(
                                description=f"Welcome to `{member.guild}` {member.mention} make sure to check out the server rules, and have a great stay!",
                                color=0x9B59B6,
                        )
                        embed.set_thumbnail(url=member.avatar_url)
                        embed.set_author(name=member.name, icon_url=member.avatar_url)
                        embed.set_footer(text=member.guild, icon_url=member.guild.icon_url)
                        embed.timestamp = datetime.datetime.utcnow()

                        await member.add_roles(join_role)

                        await channel.send(embed=embed)

        #GUILD MEMBER LEAVE

        @commands.Cog.listener()
        async def on_member_leave(self, member):
                channel = discord.utils.get(member.guild.text_channels, name="welcome")
                if channel:
                        await channel.send(f"{member.mention} Has left '{member.guild}' we've been betrayed :cry:")

        #BOT MENTION

        @commands.Cog.listener()
        async def on_message(self, message):
                if self.client.user.mentioned_in(message):
                        embed = discord.Embed(title = f"Prefix {config.prefix}", description=f"Hey! my name is {self.client.user} im a [Discord Bot](https://support.discord.com/hc/en-us/articles/212889058-Discord-s-Official-API) you can check my commands list with {config.prefix}Help at anytime!",color=0x9B59B6,)

                        embed.set_author(name="IVRY Info", icon_url=self.client.user.avatar_url)
                        embed.set_thumbnail(url=self.client.user.avatar_url)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                        embed.add_field(name = "Additional Resources", value=":video_game: [IVRY Server](https://discord.gg/ppn2u99)\n:iphone: [Website](https://ivry.tk)", inline=False)

                        await message.channel.send(embed=embed)

        #USER ERROR MESSAGES 
        
        @commands.Cog.listener() 
        async def on_command_error(self, ctx, error):

                if hasattr(ctx.command, 'on_error'):
                        return

                cog = ctx.cog
                if cog:
                        if cog._get_overridden_method(cog.cog_command_error) is not None:
                                return

                ignored = (commands.CommandNotFound)

                error = getattr(error, 'original', error)

                if isinstance(error, ignored):
                        return
                
                #USER ERROR MESSAGES

                elif isinstance(error, commands.NoPrivateMessage):
                        try:
                                await ctx.author.send(f':x: {config.prefix}`{ctx.command}` Can not be used in Private Messages.')
                        except discord.HTTPException:
                                pass

                elif isinstance(error, commands.NSFWChannelRequired):
                        await ctx.send(f':x: {config.prefix}`{ctx.command}` Can only be used in a NSFW chat or Private Messages.')

                #BOT ERROR MESSAGES

                elif isinstance(error, commands.CommandError):
                        embed = discord.Embed(title=f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal Command Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                        
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal Command Error occured in execution of {ctx.command}')
                        print(f'[ERROR] {error}')

                elif isinstance(error, commands.ConversionError):
                        embed = discord.Embed(title = f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal Command Conversion Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                        
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal Conversion Error occured in execution of {ctx.command}')
                        print(f'[ERROR] {error}')

                elif isinstance(error, commands.CheckFailure):
                        embed = discord.Embed(title = f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal Command Check Failure Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                        
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal Check Failure Error occured in execution of {ctx.command}')
                        print(f'[ERROR] {error}')

                elif isinstance(error, commands.CheckAnyFailure):
                        embed = discord.Embed(title = f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal Check Any Failure Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                        
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal Check Any Failure Error occured in execution of {ctx.command}')
                        print(f'[ERROR] {error}')

                elif isinstance(error, commands.BadBoolArgument):
                        embed = discord.Embed(title = f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal Bad Bool Arg Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                        
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal Bad Bool Arg Error occured in execution of {ctx.command}')
                        print(f'[ERROR] {error}')

                elif isinstance(error, commands.ExtensionAlreadyLoaded):
                        embed = discord.Embed(title = f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal EXT Already Loaded Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                        
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal Extension Already Loaded Error occured in execution of {ctx.command}')
                        print(f'[ERROR] {error}')

                elif isinstance(error, commands.ExtensionNotLoaded):
                        embed = discord.Embed(title = f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal EXT Not Loaded Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                        
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal Extension Not Loaded Error occured in execution of {ctx.command}')
                        print(f'[ERROR] {error}')

                elif isinstance(error, commands.NoEntryPointError):
                        embed = discord.Embed(title = f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal No Entry Point Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                        
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal No Entrypoint Error occured in execution of {ctx.command}')
                        print(f'[ERROR] {error}')

                elif isinstance(error, commands.ExtensionFailed):
                        embed = discord.Embed(title = f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal EXT Failed Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                        
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal Extension Failed Error occured in execution of {ctx.command}')
                        print(f'[ERROR] {error}')

                elif isinstance(error, commands.CommandRegistrationError):
                        embed = discord.Embed(title = f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal Command Registration Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                        
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal Command Registration Error occured in execution of {ctx.command}')
                        print(f'[ERROR] {error}')

                else:
                        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
                        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)  

def setup(client):
    client.add_cog(Events(client))