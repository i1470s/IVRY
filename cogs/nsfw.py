import discord
import logging
import praw
import aiohttp
from discord.ext import commands
from aiohttp import request
r = praw.Reddit(client_id="7oE7yB5GJJua2Q", client_secret="ooidPB-ETJxbRflpja6a65KX03g", user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36', username="PhantomVipermon")
logger = logging.getLogger("ivry")
logger.debug("nsfw.py Started")

class NSFW(commands.Cog):   
    
    def __init__(self, client):
        self.client = client
        self.session = aiohttp.ClientSession(loop=self.client.loop)

    #ASS

    @commands.command(name='ass', description="Sends some ass")
    @commands.is_nsfw()
    async def ass(self, ctx):

        async with self.session.get("https://www.reddit.com/r/buttplug/top.json?limit=1") as resp:
            ass = await resp.json()

        embed = discord.Embed(title = f'Heres Your Ass', colour=discord.Colour.purple())
        embed.set_image(url=ass['data']['children'][0]['data']['url'])
        await ctx.send(embed=embed)

    #BOOBS

    @commands.command(name='boobs', description="Sends some boobs")
    @commands.is_nsfw()
    async def boobs(self, ctx):

        async with self.session.get("https://www.reddit.com/r/boobs/top.json?limit=1") as resp:
            boobs = await resp.json()

        embed = discord.Embed(title = f'Heres Your Boobs', colour=discord.Colour.purple())
        embed.set_image(url=boobs['data']['children'][0]['data']['url'])
        await ctx.send(embed=embed)

    #RED

    @commands.command(name='red', description="Sends some redheads")
    @commands.is_nsfw()
    async def red(self, ctx):

        async with self.session.get("https://www.reddit.com/r/ginger/top.json?limit=1") as resp:
            red = await resp.json()

        embed = discord.Embed(title = f'Heres Your Red Heads', colour=discord.Colour.purple())
        embed.set_image(url=red['data']['children'][0]['data']['url'])
        await ctx.send(embed=embed)

    #HENTAI

    @commands.command(name='hentai', description="Sends some hentai")
    @commands.is_nsfw()
    async def hentai(self, ctx):
        
        async with self.session.get("https://nekos.life/api/v2/img/hentai") as resp:
            hentai = await resp.json()

        embed = discord.Embed(title = f'Heres Your Hentai', colour=discord.Colour.purple())
        embed.set_image(url=hentai['url'])
        await ctx.send(embed=embed)

    #LEWD

    @commands.command(name='lewd', description="Sends some lewds")
    @commands.is_nsfw()
    async def lewd(self, ctx):
        
        async with self.session.get("https://nekos.life/api/v2/img/lewd") as resp:
            lewd = await resp.json()

        embed = discord.Embed(title = f'Heres Your Lewd', colour=discord.Colour.purple())
        embed.set_image(url=lewd['url'])
        await ctx.send(embed=embed)

    #LESBIANS

    @commands.command(name='lesbians', description="Sends some lesbians")
    @commands.is_nsfw()
    async def lesbians(self, ctx):

        async with self.session.get("https://www.reddit.com/r/lesbians/top.json?limit=1") as resp:
            lesibans = await resp.json()

        embed = discord.Embed(title = f'Heres Your Lesbians', colour=discord.Colour.purple())
        embed.set_image(url=lesibans['data']['children'][0]['data']['url'])
        await ctx.send(embed=embed)

    #TEEN

    @commands.command(name='teen', description="Sends some teen porn")
    @commands.is_nsfw()
    async def teen(self, ctx):

        async with self.session.get("https://www.reddit.com/r/legalteens/top.json?limit=1") as resp:
            teen = await resp.json()

        embed = discord.Embed(title = f'Heres Your Teens', colour=discord.Colour.purple())
        embed.set_image(url=teen['data']['children'][0]['data']['url'])
        await ctx.send(embed=embed)

    #RANDOM

    @commands.command(name='random', description="Sends some random nsfw porn")
    @commands.is_nsfw()
    async def random(self, ctx):

        async with self.session.get("https://www.reddit.com/r/nsfw/top.json?limit=1") as resp:
            random = await resp.json()

        embed = discord.Embed(title = f'Heres Your NSFW', colour=discord.Colour.purple())
        embed.set_image(url=random['data']['children'][0]['data']['url'])
        await ctx.send(embed=embed)

    #PUSSY

    @commands.command(name='pussy', description="Sends some pussy")
    @commands.is_nsfw()
    async def pussy(self, ctx):

        async with self.session.get("https://www.reddit.com/r/pussy/top.json?limit=1") as resp:
            pussy = await resp.json()

        embed = discord.Embed(title = f'Heres Your Pussy', colour=discord.Colour.purple())
        embed.set_image(url=pussy['data']['children'][0]['data']['url'])
        await ctx.send(embed=embed)

    #VIDEO

    @commands.command(name='video', description="Sends some random porn video")
    @commands.is_nsfw()
    async def video(self, ctx):

        async with self.session.get("https://www.reddit.com/r/porn/top.json?limit=1") as resp:
            video = await resp.json()

        embed = discord.Embed(title = f'Heres Your Porn Video', colour=discord.Colour.purple())
        embed.set_image(url=video['data']['children'][0]['data']['url'])
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(NSFW(client))