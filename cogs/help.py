#PRIMARY IMPORTS

import discord, logging

#SECONDARY IMPORTS

from discord.ext import commands
from data import config

#LOGGING

logger = logging.getLogger("ivry")
logger.debug("help.py Started")

class Help(commands.Cog):   
    
        def __init__(self, client):
                self.client = client        

        #HELP COMMAND

        @commands.group(invoke_without_command=True)
        async def help(self, ctx):
            embed = discord.Embed(title = f"Prefix {config.prefix}", description = f"Use {config.default_prefix}help <catagory> for a list of commands", colour = 0x9B59B6)
            embed.set_thumbnail(url=ctx.bot.user.avatar_url)
            embed.set_footer(text=f"{config.version} | {config.shards}")
            embed.set_author(name="IVRY Help", icon_url=ctx.bot.user.avatar_url)

            embed.add_field(name = "General :gear:", value = "`10` General Commands", inline=False)
            embed.add_field(name = "Fun :tada:", value="`19` Fun Commands", inline=False)
            embed.add_field(name = "NSFW :x:", value="`10` NSFW Commands", inline=False)
            embed.add_field(name = "Music :musical_note:", value="`10` Music Player Commands", inline=False)
            embed.add_field(name = "Admin :hammer:", value="`6` Admin Commands", inline=False)
            embed.add_field(name = "Misc :question:", value="`0` Misc Commands", inline=False)
            embed.add_field(name = "Dev :tools:", value="`10` Dev Commands", inline=False)
            embed.add_field(name = "Additional Resources", value=":video_game: [IVRY Discord Server](https://discord.gg/ppn2u99)\n:iphone: [IVRY Website](https://ivry.tk)", inline=False)

            await ctx.send(embed = embed)

        #GENERAL SUB COMMAND

        @help.command()
        async def general(self, ctx):
            embed = discord.Embed(title = "IVRY Help - General :gear:", description = f"Prefix {config.prefix}", colour = 0x9B59B6)
            embed.set_thumbnail(url=ctx.bot.user.avatar_url)
            embed.set_footer(text=f"{config.version} | {config.shards}")

            embed.add_field(name = "Commands", value = "\n `about`- Bot info \n `credits`- Bot credits \n `donate`- Bot donations \n `invite`- Bot invite link \n `ping`- Bot ping \n `servers`- Bot server list \n `serverinfo`- Current serverinfo \n `userinfo`- Get user info \n `level`- Check your XP level \n `level top`- Top 10", inline=False)

            await ctx.send(embed = embed)

        #FUN SUB COMMAND
                
        @help.command()
        async def fun(self, ctx):
            embed = discord.Embed(title = "IVRY Help - Fun :tada:", description = f"Prefix {config.prefix}", colour = 0x9B59B6)
            embed.set_thumbnail(url=ctx.bot.user.avatar_url)
            embed.set_footer(text=f"{config.version} | {config.shards}")

            embed.add_field(name = "Commands", value = "\n `8ball`- Guesses your fortune \n `joke`- Sends a joke \n `djoke`- Sends a dark joke \n `meme`- Sends a meme \n `measure`- Measures your cock \n `yrn`- Yes or no \n `fortune`- Guesses your fortune \n `roll`- Roles a random number \n `useless`- Sends a useless website \n `hi`- Hey \n `fucku`- Try it \n `xmas`- Christmas countdown \n `hallow`- Halloween countdown \n `vday`- Valintines day countdown \n `ivry`- IVRYs birthday countdown \n `girlfriend`- Shoot your shot \n `boyfriend`- Shoot your shot \n `gay`- Try it \n `repeat`- Repeats what you say", inline=False)

            await ctx.send(embed = embed)

        #NSFW SUB COMMAND

        @help.command()
        async def nsfw(self, ctx):
            embed = discord.Embed(title = "IVRY Help - NSFW :x:", description = f"Prefix {config.prefix}", colour = 0x9B59B6)
            embed.set_thumbnail(url=ctx.bot.user.avatar_url)
            embed.set_footer(text=f"{config.version} | {config.shards}")

            embed.add_field(name = "Commands", value = "\n `pussy`- Sends some pussy \n `ass`- Sends some ass \n `boobs`- Sends some boobs \n `red`- Sends some gingers \n `hentai`- Sends some hentai \n `lewd`- Sends some lewd \n `lesbians`- Sends some lesbians \n `teen`- Sends some teen pussy \n `video`- Sends random porn video \n `random`- Sends some random NSFW", inline=False)

            await ctx.send(embed = embed)

        #MUSIC SUB COMMAND

        @help.command()
        async def music(self, ctx):
            embed = discord.Embed(title = "IVRY Help - Music :musical_note:", description = f"Prefix {config.prefix}", colour = 0x9B59B6)
            embed.set_thumbnail(url=ctx.bot.user.avatar_url)
            embed.set_footer(text=f"{config.version} | {config.shards}")

            embed.add_field(name = "Commands", value = "\n `join`- Join VC \n `leave`- Leave VC \n `play`- Play a song \n `skip`- Skip a song \n `queue`- Current song queue \n `shuffle`- Shuffle queue \n `remove`- Remove from queue \n `loop`- Loop song \n `now`- Currently playing \n `lyrics`- Search lyrics", inline=False)

            await ctx.send(embed = embed)

        #ADMIN SUB COMMAND

        @help.command()
        async def admin(self, ctx):
            embed = discord.Embed(title = "IVRY Help - Admin :hammer:", description = f"Prefix {config.prefix}", colour = 0x9B59B6)
            embed.set_thumbnail(url=ctx.bot.user.avatar_url)
            embed.set_footer(text=f"{config.version} | {config.shards}")

            embed.add_field(name = "Commands", value = "\n `ban`- Ban members \n `kick`- Kick members \n `mute`- Mute members \n `unban`- Unban members \n `unmute`- Unmute members \n `clear`- Clear messages", inline=False)

            await ctx.send(embed = embed)

        #MISC SUB COMMAND

        @help.command()
        async def misc(self, ctx):
            embed = discord.Embed(title = "IVRY Help - Misc :question:", description = f"Prefix {config.prefix}", colour = 0x9B59B6)
            embed.set_thumbnail(url=ctx.bot.user.avatar_url)
            embed.set_footer(text=f"{config.version} | {config.shards}")

            embed.add_field(name = "Commands", value = "\n 'Coming soon!' - SOON!", inline=False)

            await ctx.send(embed = embed)

        #DEV SUB COMMAND

        @help.command()
        async def dev(self, ctx):
            embed = discord.Embed(title = "IVRY Help - Dev :tools:", description = f"Prefix {config.prefix}", colour = 0x9B59B6)
            embed.set_thumbnail(url=ctx.bot.user.avatar_url)
            embed.set_footer(text=f"{config.version} | {config.shards}")

            embed.add_field(name = "Commands", value = "\n `leaveserver`- Leave a server \n `eval`- Compile code \n `reload`- Reload cogs \n `restart`- Restart bot \n `update` - Update bot \n `logs`- Readable logs \n `logs bot`- Bot Related logs \n `logs discord`- Discord API logs \n `logs xp`- User xp database \n `logs settings`- Guild settings database", inline=False)

            await ctx.send(embed = embed)

def setup(client):
    client.add_cog(Help(client))