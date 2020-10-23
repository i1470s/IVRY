import cogs
import random
import discord
import sys
import traceback
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext import commands

class Events(commands.Cog):   
    
        def __init__(self, client):
                self.client = client   

        #INIT

        @commands.Cog.listener()
        async def on_ready(self):
                print("Connecting To The Internet")
                print("Checking DB")
                print("Loaded Files, The Bot Is Running Normally")
                print("DONE! (Loaded)")

        #ERROR MESSAGES 
        
        @commands.Cog.listener() 
        async def on_command_error(self, ctx, error):

                if hasattr(ctx.command, 'on_error'):
                        return

                cog = ctx.cog
                if cog:
                        if cog._get_overridden_method(cog.cog_command_error) is not None:
                                return

                ignored = (commands.CommandNotFound, )

                error = getattr(error, 'original', error)

                if isinstance(error, ignored):
                        return

                if isinstance(error, commands.MissingPermissions):
                        await ctx.send(f':x: You dont have permissions to use .{ctx.command} ')

                elif isinstance(error, commands.NoPrivateMessage):
                        try:
                                await ctx.author.send(f':x: .{ctx.command} Can not be used in Private Messages.')
                        except discord.HTTPException:
                                pass

                elif isinstance(error, commands.NSFWChannelRequired):
                        await ctx.send(f':x: .{ctx.command} Can only be used in a NSFW chat or Private Messages.')

                else:
                        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
                        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

def setup(client):
    client.add_cog(Events(client))