import random
import discord
import datetime
import sys
import traceback
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext import commands
from data import config

class Events(commands.Cog):   
    
        def __init__(self, client):
                self.client = client   

        @commands.Cog.listener()
        async def on_ready(self):
                print("DONE! (Loaded Cogs)")

        #NEW SERVER

        @commands.Cog.listener()
        async def on_guild_join(self, guild):
                channel = discord.utils.get(guild.text_channels, name="general")
                if channel:
                        embed = discord.Embed(title = f"Prefix {config.prefix}", description=f"Thanks for inviting me :smile::clap:! Im happy to be apart of `{guild.name}` :tada::smile:. Make use {config.prefix}help for a list of my commands!",color=0x9B59B6,)

                embed.set_author(name="IVRY Info", icon_url=guild.me.avatar_url)
                embed.set_thumbnail(url=guild.me.avatar_url)
                embed.set_footer(text=f"{config.version} | {config.shards}")
                embed.add_field(name = "Additional Resources", value=":video_game: [IVRY Server](https://discord.gg/ppn2u99)\n:iphone: [Website](https://ivry.tk)", inline=False)

                await channel.send(embed=embed)

        #GUILD MEMBER WELCOME

        @commands.Cog.listener()
        async def on_member_join(self, member):
                role= discord.utils.get(member.guild.roles, name="Member")
                await member.add_roles(member, role)

        @commands.Cog.listener()
        async def on_member_join(self, member):
                channel = discord.utils.get(member.guild.text_channels, name="welcome")
                if channel:
                        embed = discord.Embed(
                                description=f"Welcome to our server {member.mention} make sure to check out the server rules, and have a great stay!",
                                color=0x9B59B6,
                        )
                embed.set_thumbnail(url=member.avatar_url)
                embed.set_author(name=member.name, icon_url=member.avatar_url)
                embed.set_footer(text=member.guild, icon_url=member.guild.icon_url)
                embed.timestamp = datetime.datetime.utcnow()

                await channel.send(embed=embed)

        #BOT MESSAGES (FINISH -LATER)

        @commands.Cog.listener()
        async def on_message(self, message):
                return

        #ERROR MESSAGES 
        
        @commands.Cog.listener() 
        async def on_command_error(self, ctx, error):

                if hasattr(ctx.command, 'on_error'):
                        return

                cog = ctx.cog
                if cog:
                        if cog._get_overridden_method(cog.cog_command_error) is not None:
                                return

                ignored = (commands.CommandNotFound, )

                error = getattr(error, 'original', error)

                if isinstance(error, ignored):
                        return

                if isinstance(error, commands.MissingPermissions):
                        await ctx.send(f':x: You dont have permissions to use {config.prefix}{ctx.command} ')
                
                if isinstance(error, commands.BotMissingPermissions):
                        await ctx.send(f':x: I dont have permissions to use {config.prefix}{ctx.command} please give me admin permissions.')

                elif isinstance(error, commands.NoPrivateMessage):
                        try:
                                await ctx.author.send(f':x: {config.prefix}{ctx.command} Can not be used in Private Messages.')
                        except discord.HTTPException:
                                pass

                elif isinstance(error, commands.NSFWChannelRequired):
                        await ctx.send(f':x: {config.prefix}{ctx.command} Can only be used in a NSFW chat or Private Messages.')

                else:
                        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
                        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)  

def setup(client):
    client.add_cog(Events(client))