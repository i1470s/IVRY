import discord
from discord.ext import commands
import aiohttp
from aiohttp import request

class NSFW(commands.Cog):   
    
    def __init__(self, client):
        self.client = client
        self.session = aiohttp.ClientSession(loop=self.client.loop)

    @commands.command(name='ass', description="Sends some ass")
    @commands.is_nsfw()
    async def ass(self, ctx):

        async with self.session.get("https://www.reddit.com/r/buttplug/top.json?limit=25") as resp:
            lesibans = await resp.json()

        embed = discord.Embed(title = f'Heres Your Ass', colour=discord.Colour.purple())
        embed.set_image(url=lesibans['data']['children'][0]['data']['url'])
        await ctx.send(embed=embed)

    @commands.command(name='boobs', description="Sends some boobs")
    @commands.is_nsfw()
    async def boobs(self, ctx):

        async with self.session.get("https://www.reddit.com/r/boobs/top.json?limit=25") as resp:
            lesibans = await resp.json()

        embed = discord.Embed(title = f'Heres Your Boobs', colour=discord.Colour.purple())
        embed.set_image(url=lesibans['data']['children'][0]['data']['url'])
        await ctx.send(embed=embed)

    @commands.command(name='red', description="Sends some redheads")
    @commands.is_nsfw()
    async def red(self, ctx):

        async with self.session.get("https://www.reddit.com/r/ginger/top.json?limit=25") as resp:
            lesibans = await resp.json()

        embed = discord.Embed(title = f'Heres Your Red Heads', colour=discord.Colour.purple())
        embed.set_image(url=lesibans['data']['children'][0]['data']['url'])
        await ctx.send(embed=embed)

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

        async with self.session.get("https://www.reddit.com/r/lesbians/top.json?limit=25") as resp:
            lesibans = await resp.json()

        embed = discord.Embed(title = f'Heres Your Lesbians', colour=discord.Colour.purple())
        embed.set_image(url=lesibans['data']['children'][0]['data']['url'])
        await ctx.send(embed=embed)

    @commands.command(name='teen', description="Sends some teen porn")
    @commands.is_nsfw()
    async def teen(self, ctx):

        async with self.session.get("https://www.reddit.com/r/legalteens/top.json?limit=25") as resp:
            lesibans = await resp.json()

        embed = discord.Embed(title = f'Heres Your Teens', colour=discord.Colour.purple())
        embed.set_image(url=lesibans['data']['children'][0]['data']['url'])
        await ctx.send(embed=embed)

    @commands.command(name='random', description="Sends some random nsfw porn")
    @commands.is_nsfw()
    async def random(self, ctx):

        async with self.session.get("https://www.reddit.com/r/nsfw/top.json?limit=25") as resp:
            lesibans = await resp.json()

        embed = discord.Embed(title = f'Heres Your NSFW', colour=discord.Colour.purple())
        embed.set_image(url=lesibans['data']['children'][0]['data']['url'])
        await ctx.send(embed=embed)

    @commands.command(name='pussy', description="Sends some pussy")
    @commands.is_nsfw()
    async def pussy(self, ctx):

        async with self.session.get("https://www.reddit.com/r/pussy/top.json?limit=25") as resp:
            lesibans = await resp.json()

        embed = discord.Embed(title = f'Heres Your Pussy', colour=discord.Colour.purple())
        embed.set_image(url=lesibans['data']['children'][0]['data']['url'])
        await ctx.send(embed=embed)

    @commands.command(name='video', description="Sends some random porn video")
    @commands.is_nsfw()
    async def video(self, ctx):

        async with self.session.get("https://www.reddit.com/r/porn/top.json?limit=25") as resp:
            lesibans = await resp.json()

        embed = discord.Embed(title = f'Heres Your Porn Video', colour=discord.Colour.purple())
        embed.set_image(url=lesibans['data']['children'][0]['data']['url'])
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(NSFW(client))