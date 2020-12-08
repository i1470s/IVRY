import cogs
import random
import discord
from discord.ext import commands
import platform
import time
import math
from data import config

class General(commands.Cog):   
    
        def __init__(self, client):
                self.client = client
                
        @commands.command(name='about', description="About the bot")
        async def about(self, ctx):
                try:
                         
                        embed = discord.Embed(
                                title = f'IVRY info',
                                colour = 0x9B59B6
                        )
                        embed.set_thumbnail(url=ctx.bot.user.avatar_url)

                        embed.add_field(name='Created by', value=f'I1470s#0396', inline=False)

                        embed.add_field(name='Status', value=f'Online 🟢', inline=False)

                        embed.add_field(name='Website', value=f'[Click Me](https://ivry.tk)', inline=False)

                        embed.add_field(name='Discord Server', value=f'[Click Me](https://discord.gg/ppn2U99)', inline=False)

                        embed.add_field(name='Announcements', value=f'Join Our Discord!!!!', inline=False)

                        embed.set_footer(
                        text=f"{config.version} | {config.shards}")

                        await ctx.send(embed=embed)
                except Exception as e:
                        await ctx.send(f'{e}')

        @commands.command(name='credits', description="Bot credits")
        async def credits(self, ctx):
                try:
                         
                        embed = discord.Embed(
                                title = f'IVRY Credits',
                                colour = 0x9B59B6
                        )
                        embed.add_field(name=':keyboard: Developers', value=f'[i1470s#0396](https://github.com/i1470s)')
                        embed.add_field(name=':open_hands: Contributors', value=f'[asianmin#2060](https://www.youtube.com/channel/UCWe_MB0vTXLjoXpp7D86ybA)')
                        embed.add_field(name=':books: Libraries', value=f'[Discord.py](https://github.com/Rapptz/discord.py)\n[Youtube_dl](https://github.com/ytdl-org/youtube-dl/)')
                        embed.add_field(name=':tools: Miscellaneous', value=f'[GNU(License)](http://www.gnu.org/licenses/)', inline=False)

                        await ctx.send(embed=embed)
                except Exception as e:
                        await ctx.send(f'{e}')

        @commands.command(name='donate', description="Donate to the bot")
        async def donate(self, ctx):
                try:
                         
                        embed = discord.Embed(
                                title = f'IVRY Donations',
                                colour = 0x9B59B6
                        )
                        embed.set_thumbnail(url=ctx.bot.user.avatar_url)
                        
                        embed.add_field(name=f'Donations help keep us alive!', value=f'[Click Me](https://www.paypal.com/donate/?hosted_button_id=QWT56W6DFV8H4)')


                        await ctx.send(embed=embed)
                except Exception as e:
                        await ctx.send(f'{e}')

        @commands.command(name='invite', description="Invite the bot")
        async def invite(self, ctx):
                try:
                         
                        embed = discord.Embed(
                                title = f'IVRY Invite',
                                colour = 0x9B59B6
                        )
                        embed.set_thumbnail(url=ctx.bot.user.avatar_url)
                        
                        embed.add_field(name=f'Invite IVRY to your server!', value=f'[CLick Me](https://discord.com/api/oauth2/authorize?client_id=764424676256514081&permissions=8&scope=bot)')

                        await ctx.send(embed=embed)
                except Exception as e:
                        await ctx.send(f'{e}')

        @commands.command(name='ping', description="Bot latency")
        async def ping(self, ctx):
                before = time.monotonic()
                before_ws = int(round(self.client.latency * 1000, 1))
                message = await ctx.send("🏓 Pong")
                ping = (time.monotonic() - before) * 1000
                await message.edit(content=f"🏓 WS: {before_ws}ms  |  REST: {int(ping)}ms")


        @commands.command(name='servers', description="List of bot servers")
        async def servers(self, ctx):
                msg = '```js\n'
                msg += '{!s:19s} | {!s:>5s} | {}\n'.format('ID', 'Member', 'Name')
                for guild in self.client.guilds:
                        msg += '{!s:19s} |{!s:>5s}   | {}\n'.format(guild.id, guild.member_count, guild.name)
                msg += '```'
                await ctx.send(msg)

        @commands.command(name='serverinfo', description="Shows server info")
        @commands.guild_only()
        async def serverinfo(self, ctx):
                try:
                        count = 0

                        members = await ctx.guild.fetch_members().flatten()

                        for people in members:
                                if people.bot:
                                        count = count + 1
                        else:
                                pass

                        embed = discord.Embed(
                                title = f'{ctx.guild.name} info',
                                colour = 0x9B59B6
                        )
                        embed.set_thumbnail(url=ctx.guild.icon_url)

                        embed.add_field(name='Owner name', value=f'<@{ctx.guild.owner_id}>')
                        embed.add_field(name='Server ID', value=ctx.guild.id)

                        embed.add_field(name='Server region', value=ctx.guild.region)
                        embed.add_field(name='Members', value=ctx.guild.member_count)
                        embed.add_field(name='bots', value=count)

                        embed.add_field(name='Text Channels', value=len(ctx.guild.text_channels))
                        embed.add_field(name='Voice Channels', value=len(ctx.guild.voice_channels))

                        embed.add_field(name='Created On', value=ctx.guild.created_at.strftime('%a, %#d %B %Y, %I:%M %p UTC'))

                        await ctx.send(embed=embed)
                except Exception as e:
                        await ctx.send(f'{e}')

        @commands.command(name="userinfo", description="Shows user info ")
        @commands.guild_only()    
        async def userinfo(self, ctx, member: discord.Member = None):
                if not member:  
                        member = ctx.message.author  
                embed = discord.Embed(colour=discord.Colour.purple(), timestamp=ctx.message.created_at,
                                        title=f"User Info - {member}")
                embed.set_thumbnail(url=member.avatar_url)

                embed.add_field(name="ID", value=member.id, inline=False)
                embed.add_field(name="Display Name", value=member.display_name, inline=False)

                embed.add_field(name="Created Account On", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

                await ctx.send(embed=embed)

def setup(client):
    client.add_cog(General(client))