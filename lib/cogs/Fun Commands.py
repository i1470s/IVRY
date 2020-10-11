import cogs
import random
from random import choice, randint
from typing import Optional
import discord
from discord.ext import commands
from discord.ext.commands import cooldown
import aiohttp
from aiohttp import request
import pyfiglet
import datetime
now = datetime.datetime.now()
diff = datetime.datetime(now.year, 12, 25) - \
    datetime.datetime.today()  # Days until Christmas


client = commands.Bot(command_prefix='.')

class Fun_Commands(commands.Cog):   
    
        def __init__(self, client):
                self.client = client   

        @commands.command(name='8Ball', aliases=["8ball"], description="Awnsers your questions")
        async def _8ball(self, ctx, *, question):
                responses = ['It is certain',
                        'It is decidedly so',
                        'Without a doubt',
                        'Yes Definitely',
                        'You may rely on it',
                        'Most likely',
                        'Yes',
                        'No',
                        'Dont count on it',
                        'Can not predict now',
                        'the reply is no',
                        'very doubtful']
                await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')
        
        @commands.command(name='djoke', description="Dark jokes")
        async def djoke(self, ctx):
                responses = ['america is so bad at chess they lost two towers in one move',
                        'i was digging the ground and i found gold, so i went to go tell my son, then i realized why i was digging',
                        'I have a fish that can breakdance! Only for 20 seconds though, and only once.',
                        'i was working and this kid came up to me saying his parents were gone. Damn orphans in telling you',
                        'BLM lol jk',
                        'I just read that someone in London gets stabbed every 52 seconds. Poor guy.',
                        'Whats red and bad for your teeth? A brick.',
                        'Give a man a match, and he be warm for a few hours. Set a man on fire, and he will be warm for the rest of his life.',
                        'Even people who are good for nothing have the capacity to bring a smile to your face. For instance, when you push them down the stairs.',
                        'Never break someones heart, they only have one. Break their bones instead, they have 206 of them.',
                        'Today was a terrible day. My ex got hit by a bus. And I lost my job as a bus driver!',
                        'An apple a day keeps the doctor away. Or at least it does if you throw it hard enough.',
                        'you can only skydive without a parachute once']
                await ctx.send(f'{random.choice(responses)}')

        @commands.command(name='meme', description="Sends a meme")
        async def meme(self, ctx):

                colour_choices= [0x9B59B6]

                meme_url = "https://meme-api.herokuapp.com/gimme?"
                async with request("GET", meme_url, headers={}) as response:
                        if response.status==200:
                                data = await response.json()
                                image_link = data["url"]
                        else:
                                image_link = None

                        async with request("GET", meme_url, headers={}) as response:
                                if response.status==200:
                                        data = await response.json()
                                        embed = discord.Embed(
                                        title=data["title"],
                                        colour=random.choice(colour_choices),
                                        )
                                        if image_link is not None:
                                                embed.set_image(url=image_link)
                                                await ctx.send(embed=embed)

                                        else:
                                                await ctx.send(f"The API seems down, says {response.status}")

        @commands.command(name='xmas', discription='Xmas countdown')
        async def xmas(self, ctx):
                await ctx.send("**{0}** day(s) left until Christmas day! :christmas_tree:".format(str(diff.days)))

        @commands.command(name='girlfriend', description="Take your shot")
        async def girlfriend(self, ctx):
                await ctx.send(f'Lol you wish')

        @commands.command(name='measure', description="Measures your cock")
        async def measure(self, ctx):
                responses = ['1 inches',
                        '2 inches',
                        '3 inches',
                        '4 inches',
                        '5 inches',
                        '6 inches',
                        '7 inches',
                        '8 inches',
                        '9 inches',
                        '10 inches',
                        '11 inches',
                        '12 inches',]
                await ctx.send(f'Whoa You Got {random.choice(responses)}')
        
        @commands.command(name='joke', description="Tells you a joke")
        async def joke(self, ctx):
                responses = ['The machine at the coin factory just suddenly stopped working, with no explanation. It doesnt make any cents!',
                        'I was going to make myself a belt made out of watches, but then I realized it would be a waist of time.',
                        'Yesterday, a clown held the door open for me. It was such a nice jester!',
                        'Did you hear about the man who was accidentally buried alive?  It was a grave mistake.',
                        'A Canadian psychologist is selling a video that teaches you how to test your dogs IQ. Here’s how it works: If you spend $12.99 for the video, your dog is smarter than you. Jay Leno',
                        'What’s the tallest building in the world? The library, cause it has the most stories.',
                        'How do trees get online? They log in.',
                        'What do you call a bear with no teeth? A gummy bear.',
                        'What’s the difference between snowmen and snow women? Snowballs.',
                        'Why did the picture go to jail? Because it was framed',
                        'How do you tease fruit? Banananananananana!',
                        'Why did Goofy put a clock under his desk? Because he wanted to work over-time!',
                        'Why did Tommy throw the clock out of the window? Because he wanted to see time fly!',
                        'How does a moulded fruit-flavoured dessert answer the phone? Jell-o!',
                        'When do you stop at green and go at red? When you’re eating a watermelon!',
                        'What’s the difference between a cat and a complex sentence?A cat has claws at the end of its paws. A complex sentence has a pause at the end of its clause.',
                        'How do you repair a broken tomato? Tomato Paste!',
                        'there’s a plane heading straight for the ground which there was no guarantee of surviving there was a cowboy, an asian, and a canadian on board the cowboy threw out his cowboy hat saying i have too many of these in my country. the asian threw out his textbook saying i have too many of these in my country. the canadian threw the asian out saying i have too many of these in my country',]

                await ctx.send(f'{random.choice(responses)}')

        @commands.command(name='fortune', description="Checks your fortune")
        async def fortune(self, ctx):
                responses = ['$1 Dollar',
                        '$2000 Dollars',
                        '$0 Dollars',
                        '$100000 Dollars',
                        '$6 Dollars',
                        '$18.95 Dollars',
                        '$5 Dollars',
                        '$900 Dollars',
                        '$21 Dollars',
                        '$420 Dollars',
                        '$69 Dollars',
                        '$1000000 Dollars',]
                await ctx.send(f'You Got {random.choice(responses)}')
        
        @commands.command(name='roll', description="Rolls a dice")
        async def roll(self, ctx):
                responses = ['1',
                        '2',
                        '3',
                        '4',
                        '5',
                        '6',
                        '7',
                        '8',
                        '9',
                        '10',
                        '11',
                        '12',]
                await ctx.send(f'You Got {random.choice(responses)}')

        @commands.command(name='useless', description="Links useless websites")
        async def useless(self, ctx):
                responses = ['http://chihuahuaspin.com/',
                        'http://www.staggeringbeauty.com/',
                        'https://leekspin.com/',
                        'http://whitetrash.nl/',
                        'http://yeahlemons.com/',
                        'http://dogs.are.the.most.moe/',
                        'http://www.ouaismaisbon.ch/',
                        'http://www.muchbetterthanthis.com/',
                        'https://crouton.net/',
                        'https://semanticresponsiveillustration.com/',
                        'http://www.partridgegetslucky.com/',
                        'http://www.trashloop.com/',
                        'http://willthefuturebeaweso.me/',
                        'https://r33b.net/',
                        'http://spaceis.cool/',
                        'http://www.fallingfalling.com/',
                        'http://corndogoncorndog.com/',
                        'http://ww12.infinitething.com/',
                        'https://chrismckenzie.com/',
                        'http://onemillionlols.com/',
                        'https://iamawesome.com/',]
                try:
                        embed = discord.Embed(
                                colour = 0x9B59B6
                        )
                        embed.add_field(name='Here is your useless website:', value=f'{random.choice(responses)}', inline=False)

                        await ctx.send(embed=embed)
                except Exception as e:
                                await ctx.send(f'{e}')

                return

def setup(client):
    client.add_cog(Fun_Commands(client))