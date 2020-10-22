from discord.ext import commands
import aiohttp
import discord
import random
import praw
r = praw.Reddit(client_id="7oE7yB5GJJua2Q", client_secret="ooidPB-ETJxbRflpja6a65KX03g", user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36', username="PhantomVipermon")
from aiohttp import request

client = commands.Bot(command_prefix='.')

class NSFW(commands.Cog):   
    
    def __init__(self, client):
        self.client = client
        self.session = aiohttp.ClientSession(loop=self.client.loop)

    @commands.command(name='ass', description="Sends some ass")
    @commands.is_nsfw()
    async def ass(self, ctx):

        if hasattr(ctx.message.channel, "nsfw"):
            channel_nsfw = ctx.message.channel.nsfw
        else:
            channel_nsfw = str(ctx.message.channel.type) == "private"

        if channel_nsfw:
            sub = r.subreddit('buttplug')
            await ctx.send(sub.random().url)

    @commands.command(name='boobs', description="Sends some boobs")
    @commands.is_nsfw()
    async def boobs(self, ctx):

        if hasattr(ctx.message.channel, "nsfw"):
            channel_nsfw = ctx.message.channel.nsfw
        else:
            channel_nsfw = str(ctx.message.channel.type) == "private"

        if channel_nsfw:
            sub = r.subreddit('boobs')
            await ctx.send(sub.random().url)

    @commands.command(name='red', description="Sends some redheads")
    @commands.is_nsfw()
    async def red(self, ctx):

        if hasattr(ctx.message.channel, "nsfw"):
            channel_nsfw = ctx.message.channel.nsfw
        else:
            channel_nsfw = str(ctx.message.channel.type) == "private"

        if channel_nsfw:
            sub = r.subreddit('ginger')
            await ctx.send(sub.random().url)

    @commands.command(name='hentai', description="Sends some hentai")
    @commands.is_nsfw()
    async def hentai(self, ctx):
        
        async with self.session.get("https://nekos.life/api/v2/img/hentai") as resp:
            nekos = await resp.json()

        embed = discord.Embed(title = f'Heres Your Hentai', colour=discord.Colour.purple())
        embed.set_image(url=nekos['url'])
        await ctx.send(embed=embed)

    @commands.command(name='lewd', description="Sends some lewds")
    @commands.is_nsfw()
    async def lewd(self, ctx):
        
        async with self.session.get("https://nekos.life/api/v2/img/lewd") as resp:
            nekos = await resp.json()

        embed = discord.Embed(title = f'Heres Your Lewd', colour=discord.Colour.purple())
        embed.set_image(url=nekos['url'])
        await ctx.send(embed=embed)


    @commands.command(name='lesbians', description="Sends some lesbians")
    @commands.is_nsfw()
    async def lesbians(self, ctx):

        if hasattr(ctx.message.channel, "nsfw"):
            channel_nsfw = ctx.message.channel.nsfw
        else:
            channel_nsfw = str(ctx.message.channel.type) == "private"

        if channel_nsfw:
            sub = r.subreddit('lesbians')
        await ctx.send(sub.random().url)

    @commands.command(name='teen', description="Sends some teen pussy")
    @commands.is_nsfw()
    async def teen(self, ctx):

        if hasattr(ctx.message.channel, "nsfw"):
            channel_nsfw = ctx.message.channel.nsfw
        else:
            channel_nsfw = str(ctx.message.channel.type) == "private"

        if channel_nsfw:
            sub = r.subreddit('LegalTeens')
        await ctx.send(sub.random().url)

    @commands.command(name='random', description="Sends some random nsfw")
    @commands.is_nsfw()
    async def random(self, ctx):

        if hasattr(ctx.message.channel, "nsfw"):
            channel_nsfw = ctx.message.channel.nsfw
        else:
            channel_nsfw = str(ctx.message.channel.type) == "private"

        if channel_nsfw:
            sub = r.subreddit('nsfw')
        await ctx.send(sub.random().url)

    @commands.command(name='pussy', description="Sends some pussy")
    @commands.is_nsfw()
    async def pussy(self, ctx):

        if hasattr(ctx.message.channel, "nsfw"):
            channel_nsfw = ctx.message.channel.nsfw
        else:
            channel_nsfw = str(ctx.message.channel.type) == "private"

        if channel_nsfw:
            sub = r.subreddit('pussy')
        await ctx.send(sub.random().url)

def setup(client):
    client.add_cog(NSFW(client))