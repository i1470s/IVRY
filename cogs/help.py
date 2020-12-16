import random
import discord
import math
from discord.ext import commands
from data import config

class Help(commands.Cog):   
    
        def __init__(self, client):
                self.client = client        

        @commands.group(invoke_without_command=True)
        async def help(self, ctx):
            embed = discord.Embed(title = f"Prefix {config.prefix}", description = f"Use {config.default_prefix}help <catagory> for a list of commands", colour = 0x9B59B6)
            embed.set_thumbnail(url=ctx.bot.user.avatar_url)
            embed.set_footer(text=f"{config.version} | {config.shards}")
            embed.set_author(name="IVRY Help", icon_url=ctx.bot.user.avatar_url)

            embed.add_field(name = "General :gear:", value = "`8` General Commands", inline=False)
            embed.add_field(name = "Fun :tada:", value="`17` Fun Commands", inline=False)
            embed.add_field(name = "NSFW :x:", value="`9` NSFW Commands", inline=False)
            embed.add_field(name = "Music :musical_note:", value="`10` Music Player Commands", inline=False)
            embed.add_field(name = "Admin :hammer:", value="`6` Admin Commands", inline=False)
            embed.add_field(name = "Additional Resources", value=":video_game: [IVRY Server](https://discord.gg/ppn2u99)\n:iphone: [Website](https://ivry.tk)", inline=False)

            await ctx.send(embed = embed)

        @help.command()
        async def general(self, ctx):
            embed = discord.Embed(title = "IVRY Help - General :gear:", description = f"Prefixes {config.prefix}", colour = 0x9B59B6)
            embed.set_thumbnail(url=ctx.bot.user.avatar_url)
            embed.set_footer(text=f"{config.version} | {config.shards}")

            embed.add_field(name = "Commands", value = "\n `about`- Bot info \n `credits`- Bot credits \n `donate`- Bot donations \n `invite`- Bot invite link \n `ping`- Bot ping \n `servers`- Bot server list \n `serverinfo`- Current serverinfo \n `userinfo`- Get user info", inline=False)

            await ctx.send(embed = embed)

        @help.command()
        async def fun(self, ctx):
            embed = discord.Embed(title = "IVRY Help - Fun :tada:", description = f"Prefixes {config.prefix}", colour = 0x9B59B6)
            embed.set_thumbnail(url=ctx.bot.user.avatar_url)
            embed.set_footer(text=f"{config.version} | {config.shards}")

            embed.add_field(name = "Commands", value = "\n `8ball`- Guesses your fortune \n `joke`- Sends a joke \n `djoke`- Sends a dark joke \n `meme`- Sends a meme \n `measure`- Measures your cock \n `fortune`- Guesses your fortune \n `roll`- Roles a random number \n `useless`- Sends a useless website \n `hi`- Hey \n `fucku`- Try it \n `xmas`- Christmas countdown \n `hallow`- Halloween countdown \n `vday`- Valintines day countdown \n `girlfriend`- Shoot your shot \n `boyfriend`- Shoot your shot \n `gay`- Try it \n `repeat`- Repeats what you say", inline=False)

            await ctx.send(embed = embed)

        @help.command()
        async def nsfw(self, ctx):
            embed = discord.Embed(title = "IVRY Help - NSFW :x:", description = f"Prefixes {config.prefix}", colour = 0x9B59B6)
            embed.set_thumbnail(url=ctx.bot.user.avatar_url)
            embed.set_footer(text=f"{config.version} | {config.shards}")

            embed.add_field(name = "Commands", value = "\n `ass`- Sends some ass \n `boobs`- Sends some boobs \n `red`- Sends some gingers \n `hentai`- Sends some hentai \n `lewd`- Sends some lewd \n `lesbians`- Sends some lesbians \n `teen`- Sends some teen pussy \n `random`- Sends some random NSFW \n `pussy`- Sends some pussy", inline=False)

            await ctx.send(embed = embed)

        @help.command()
        async def music(self, ctx):
            embed = discord.Embed(title = "IVRY Help - Music :musical_note:", description = f"Prefixes {config.prefix}", colour = 0x9B59B6)
            embed.set_thumbnail(url=ctx.bot.user.avatar_url)
            embed.set_footer(text=f"{config.version} | {config.shards}")

            embed.add_field(name = "Commands", value = "\n`join`- Join VC \n `leave`- Leave VC \n `play`- Play a song \n `skip`- Skip a song \n `queue`- Current song queue \n `shuffle`- Shuffle queue \n `remove`- Remove from queue \n `loop`- Loop song \n `now`- Currently playing \n `lyrics`- Search lyrics", inline=False)

            await ctx.send(embed = embed)

        @help.command()
        async def admin(self, ctx):
            embed = discord.Embed(title = "IVRY Help - Admin :hammer:", description = f"Prefixes {config.prefix}", colour = 0x9B59B6)
            embed.set_thumbnail(url=ctx.bot.user.avatar_url)
            embed.set_footer(text=f"{config.version} | {config.shards}")
            
            embed.add_field(name = "Commands", value = "\n `ban`- Ban members \n `kick`- Kick members \n `mute`- Mute members \n `unban`- Unban members \n `unmute`- Unmute members \n `clear`- Clear messages", inline=False)

            await ctx.send(embed = embed)

def setup(client):
    client.add_cog(Help(client))