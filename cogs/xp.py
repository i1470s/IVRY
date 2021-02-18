import discord, json, os, datetime, asyncio, logging
from discord.ext import commands, tasks
from random import randint
from data import config
logger3 = logging.getLogger("ivry")
logger3.debug("xp.py Started")
logger3.debug(f"--------COMPLETE IVRY {config.version}-------")
logger3.debug("")

epoch = datetime.datetime.utcfromtimestamp(0)
time_diff = round((datetime.datetime.utcnow() - epoch).total_seconds())

#CREATES NEW USER DATA + ADDS XP 

class xp(commands.Cog):

    def __init__(self, client):
        self.client = client

        with open(r"./data/dbs/users-xp.json", "r") as f:
            self.users = json.load(f)

        self.client.loop.create_task(self.save_users())

    async def save_users(self):
        await self.client.wait_until_ready()
        while not self.client.is_closed():
            with open(r"./data/dbs/users-xp.json", "w") as f:
                json.dump(self.users, f, indent=4)

            await asyncio.sleep(5)

    def lvl_up(self, author_id):
        cur_xp = self.users[author_id]["exp"]
        cur_lvl = self.users[author_id]["level"]

        if cur_xp >= round((4 * (cur_lvl ** 3)) / 5):
            self.users[author_id]["level"] += 1
            return True
        else:
            return False

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return

        author_id = str(message.author.id)

        if not author_id in self.users:
            self.users[author_id] = {}
            self.users[author_id]["level"] = 0
            self.users[author_id]["exp"] = 0

        self.users[author_id]["exp"] += 1

        if self.lvl_up(author_id):
            await message.channel.send(f"{message.author.mention} is now level {self.users[author_id]['level']}")
    
    #LEVEL

    @commands.group(invoke_without_command=True)
    async def level(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        member_id = str(member.id)

        if not member_id in self.users:
            await ctx.send(f"{member} doesn't have a level")
        else:
            embed = discord.Embed(title=f"{member} Stats",color=0x9B59B6, timestamp=ctx.message.created_at)

            embed.set_author(name=f"IVRY Level", icon_url=self.client.user.avatar_url)

            embed.set_thumbnail(url=member.avatar_url)
            embed.add_field(name="Level", value=self.users[member_id]["level"])
            embed.add_field(name="XP", value=self.users[member_id]["exp"])

            await ctx.send(embed=embed)
    
    #LEVEL TOP SUB COMMAND - FIX ME BY V.3.0

    @level.command()
    async def top(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        member_id = str(member.id)
        try:
            embed = discord.Embed(title=f"`{ctx.guild.name}`'s Top 10 Members",color=0x9B59B6, timestamp=ctx.message.created_at)

            embed.set_author(name=f"IVRY Level", icon_url=self.client.user.avatar_url)

            embed.set_thumbnail(url=self.client.user.avatar_url)
            embed.add_field(name="Coming Soon", value="This just shows your stats for now i am currently working on this!")
            embed.add_field(name="Level", value=self.users[member_id]["level"])
            embed.add_field(name="XP", value=self.users[member_id]["exp"])

            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send(f'{e}')

def setup(client):
    client.add_cog(xp(client))