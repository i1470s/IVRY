import discord, datetime, logging
from discord.ext import commands
from data import config
logger3 = logging.getLogger("ivry")
logger3.debug("events.py Started")

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
                        embed.add_field(name = "Additional Resources", value=":video_game: [IVRY Discord Server](https://discord.gg/ppn2u99)\n:iphone: [IVRY Website](https://ivry.tk)", inline=False)

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
                        embed.add_field(name = "Additional Resources", value=":video_game: [IVRY Discord Server](https://discord.gg/ppn2u99)\n:iphone: [IVRY Website](https://ivry.tk)", inline=False)

                        await message.channel.send(embed=embed) 

def setup(client):
    client.add_cog(Events(client))