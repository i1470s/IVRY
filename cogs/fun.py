import discord, random, math, aiohttp, datetime, logging
from random import choice, randint
from typing import Optional
from discord.ext import commands
from discord.ext.commands import cooldown
from aiohttp import request
now = datetime.datetime.now()
diff = datetime.datetime(now.year, 12, 25) - \
    datetime.datetime.today() 
diff2 = datetime.datetime(now.year, 10, 31) - \
    datetime.datetime.today() 
diff3 = datetime.datetime(now.year, 2, 14) - \
    datetime.datetime.today() 
diff4 = datetime.datetime(now.year, 7, 13) - \
    datetime.datetime.today() 
logger = logging.getLogger("ivry")
logger.debug("fun.py Started")

class Fun(commands.Cog):   
    
        def __init__(self, client):
                self.client = client   
        
        #8BALL

        @commands.command(name='8Ball', description="Awnsers your questions")
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
        
        #JOKE

        @commands.command(name='joke', description="Tells you a joke")
        async def joke(self, ctx):

                colour_choices= [0x9B59B6]

                meme_url = "https://sv443.net/jokeapi/v2/joke/Miscellaneous,Pun,Spooky,Christmas?type=single"
                async with request("GET", meme_url, headers={}) as response:
                        if response.status==200:
                                data = await response.json()
                                joke = data["joke"]

                                await ctx.send(f"{joke}")

                        else:
                                await ctx.send(f"The API seems down, says {response.status}")

        #DJOKE

        @commands.command(name='djoke', description="Dark jokes")
        async def djoke(self, ctx):

                colour_choices= [0x9B59B6]

                meme_url = "https://sv443.net/jokeapi/v2/joke/Dark?type=single"
                async with request("GET", meme_url, headers={}) as response:
                        if response.status==200:
                                data = await response.json()
                                joke = data["joke"]

                                await ctx.send(f"{joke}")

                        else:
                                await ctx.send(f"The API seems down, says {response.status}")

        #MEME

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

        #MEASURE

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

        #FORTUNE

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

        #ROLL

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

        #YRN

        @commands.command(name='yrn', description="Yes or no")
        async def yrn(self, ctx):
                responses = ['Yes',
                        'No',]
                await ctx.send(f'The awnser is {random.choice(responses)}')

        #USELESS

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
        #HI

        @commands.command(name='hi', description="Hello :)")
        async def hi(self, ctx):
                await ctx.send(f'Hello :)')

        #FUCKU

        @commands.command(name='fucku', description="Try it :p")
        async def fucku(self, ctx):
                await ctx.send(f'No Fuck You')
        
        #XMAS

        @commands.command(name='xmas', description='Xmas countdown')
        async def xmas(self, ctx):
                await ctx.send("**{0}** day(s) left until Christmas day! :christmas_tree:".format(str(diff.days)))

        #HALLOW

        @commands.command(name='hallow', description='Halloween countdown')
        async def boo(self, ctx):
                await ctx.send("**{0}** day(s) left until Halloween! :candy:".format(str(diff2.days)))
        
        #VDAY

        @commands.command(name='vday', description='Valentines countdown')
        async def vday(self, ctx):
                await ctx.send("**{0}** day(s) left until Valentines day! :heart:".format(str(diff3.days)))

        #IVRY

        @commands.command(name='IVRY', description='ivry bday countdown')
        async def ivry(self, ctx):
                await ctx.send("**{0}** day(s) left until ivrys bday! :tada:".format(str(diff4.days)))

        #GIRLFRIEND

        @commands.command(name='girlfriend', description="Take your shot")
        async def girlfriend(self, ctx):
                await ctx.send(f'Lol your dreaming you disrespecful trash!!!')

        #BOYFRIEND

        @commands.command(name='boyfriend', description="Take your shot")
        async def boyfriend(self, ctx):
                await ctx.send(f'Lol you think someone would want you????')

        #GAY

        @commands.command(name='gay', description="Take the test")
        async def gay(self, ctx, member: discord.Member = None):        
                await ctx.send(f'Lemme check... ohhh its u lol, dumbass')

        #REPEAT

        @commands.command(name='repeat', description="Repeats you")
        async def repeat(self, ctx, *, message):
                await ctx.send(message)  

def setup(client):
    client.add_cog(Fun(client))