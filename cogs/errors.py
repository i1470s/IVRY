import discord, os, datetime, sys, json, traceback, logging
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext import commands
from data import config
logger = logging.getLogger("ivry")
logger.debug("errors.py Started")

class Errors(commands.Cog):   
    
        def __init__(self, client):
                self.client = client

        #ERROR MESSAGES 
        
        @commands.Cog.listener() 
        async def on_command_error(self, ctx, error):

                if hasattr(ctx.command, 'on_error'):
                        return

                cog = ctx.cog
                if cog:
                        if cog._get_overridden_method(cog.cog_command_error) is not None:
                                return

                ignored = (commands.CommandNotFound)

                error = getattr(error, 'original', error)

                if isinstance(error, ignored):
                        return

        #COMMAND ERROR

                elif isinstance(error, commands.CommandError):
                        embed = discord.Embed(title=f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal Command Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                        
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal Command Error occured in execution of {ctx.command}')
                        logger.debug(f"[ERROR] {ctx.command} | {error}")

        #CONVERSION ERROR

                elif isinstance(error, commands.ConversionError):
                        embed = discord.Embed(title = f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal Command Conversion Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                        
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal Conversion Error occured in execution of {ctx.command}')
                        logger.debug(f"[ERROR] {ctx.command} | {error}")
        
        #USER INPUT ERROR

                elif isinstance(error, commands.UserInputError):
                        embed = discord.Embed(title = f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal User Input Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                        
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal User Input Error occured in execution of {ctx.command}')
                        logger.debug(f"[ERROR] {ctx.command} | {error}")

        #MISSING REQUIRED ARGUMENT
                
                elif isinstance(error, commands.MissingRequiredArgument):
                        embed = discord.Embed(title = f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal Command Conversion Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                        
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal Conversion Error occured in execution of {ctx.command}')
                        logger.debug(f"[ERROR] {ctx.command} | {error}")

        #TOO MANY ARGUMENTS
                elif isinstance(error, commands.TooManyArguments):
                        embed = discord.Embed(title = f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal Command Conversion Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                        
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal Conversion Error occured in execution of {ctx.command}')
                        logger.debug(f"[ERROR] {ctx.command} | {error}")

        #BAD ARGUMENT

                elif isinstance(error, commands.BadArgument):
                        embed = discord.Embed(title = f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal Bad Argument Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                                        
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal Bad Argument Error occured in execution of {ctx.command}')
                        logger.debug(f"[ERROR] {ctx.command} | {error}")     

                #MESSAGE NOT FOUND

                elif isinstance(error, commands.MessageNotFound):
                        embed = discord.Embed(title = f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal Message Not Found Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                                        
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal Message Not Found Error occured in execution of {ctx.command}')
                        logger.debug(f"[ERROR] {ctx.command} | {error}")     

                #MEMBER NOT FOUND

                elif isinstance(error, commands.MemberNotFound):
                        embed = discord.Embed(title = f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal Member Not Found Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                                        
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal Bad Member Not Found occured in execution of {ctx.command}')
                        logger.debug(f"[ERROR] {ctx.command} | {error}")    

                #USER NOT FOUND

                elif isinstance(error, commands.UserNotFound):
                        embed = discord.Embed(title = f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal User Not Found Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                                        
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal User Not Found Error occured in execution of {ctx.command}')
                        logger.debug(f"[ERROR] {ctx.command} | {error}")  

                #CHANNEL NOT FOUND

                elif isinstance(error, commands.ChannelNotFound):
                        embed = discord.Embed(title = f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal Channel Not Found Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                                        
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal Channel Not Found Error occured in execution of {ctx.command}')
                        logger.debug(f"[ERROR] {ctx.command} | {error}")  

                #CHANNEL NOT READABLE

                elif isinstance(error, commands.ChannelNotReadable):
                        embed = discord.Embed(title = f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal Channel Not Readable Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                                        
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal Channel Not Readable Error occured in execution of {ctx.command}')
                        logger.debug(f"[ERROR] {ctx.command} | {error}")  

                #BAD COLOR ARGUMENT

                elif isinstance(error, commands.BadColourArgument):
                        embed = discord.Embed(title = f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal Bad Colour Argument Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                                        
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal Bad Colour Argument Error occured in execution of {ctx.command}')
                        logger.debug(f"[ERROR] {ctx.command} | {error}") 

                #ROLE NOT FOUND

                elif isinstance(error, commands.RoleNotFound):
                        embed = discord.Embed(title = f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal Role Not Found Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                        
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal Role Not Found Error occured in execution of {ctx.command}')
                        logger.debug(f"[ERROR] {ctx.command} | {error}")

                #BAD INVITE ARGUMENT
                
                elif isinstance(error, commands.BadInviteArgument):
                        embed = discord.Embed(title = f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal Command Conversion Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                        
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal Conversion Error occured in execution of {ctx.command}')
                        logger.debug(f"[ERROR] {ctx.command} | {error}")

                #EMOJI NOT FOUND

                elif isinstance(error, commands.EmojiNotFound):
                        embed = discord.Embed(title = f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal Emoji Not Found Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                        
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal Emoji Not Found Error occured in execution of {ctx.command}')
                        logger.debug(f"[ERROR] {ctx.command} | {error}")

                #PARTIAL EMOJI CONVERSION FAILURE

                elif isinstance(error, commands.PartialEmojiConversionFailure):
                        embed = discord.Embed(title = f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal Partial Emoji Conversion Failure Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                        
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal Partial Emoji Conversion Failure Error occured in execution of {ctx.command}')
                        logger.debug(f"[ERROR] {ctx.command} | {error}")

                #BAD BOOL ARGUMENT

                elif isinstance(error, commands.BadBoolArgument):
                        embed = discord.Embed(title = f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal Bad Bool Argument Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                        
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal Bad Bool Argument Error occured in execution of {ctx.command}')
                        logger.debug(f"[ERROR] {ctx.command} | {error}")  

                #BAD UNION ARGUMENT

                elif isinstance(error, commands.BadUnionArgument):
                        embed = discord.Embed(title = f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal Bad Union Argument Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                        
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal Bad Union Argument Error occured in execution of {ctx.command}')
                        logger.debug(f"[ERROR] {ctx.command} | {error}")  

                #ARGUMENT PARSING ERROR

                elif isinstance(error, commands.ArgumentParsingError):
                        embed = discord.Embed(title = f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal Argument Parsing Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                        
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal Argument Parsing Error occured in execution of {ctx.command}')
                        logger.debug(f"[ERROR] {ctx.command} | {error}")  

                #UNEXPECTED QUOTE ERROR

                elif isinstance(error, commands.UnexpectedQuoteError):
                        embed = discord.Embed(title = f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal Unexpected Quote Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                        
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal Unexpected Quote Error occured in execution of {ctx.command}')
                        logger.debug(f"[ERROR] {ctx.command} | {error}")  

                #INVALID END OF QUOTED STRING 

                elif isinstance(error, commands.InvalidEndOfQuotedStringError):
                        embed = discord.Embed(title = f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal Invalid End Of Quoted String Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                        
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal Invalid End Of Quoted String Error occured in execution of {ctx.command}')
                        logger.debug(f"[ERROR] {ctx.command} | {error}")

                #EXPECTED CLOSING QUOTE ERROR

                elif isinstance(error, commands.ExpectedClosingQuoteError):
                        embed = discord.Embed(title = f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal Expected Closing Quote Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                        
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal Expected Closing Quote Error occured in execution of {ctx.command}')
                        logger.debug(f"[ERROR] {ctx.command} | {error}")
                
        #COMMAND NOT FOUND

                elif isinstance(error, commands.CommandNotFound):
                        embed = discord.Embed(title = f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal Command Not Found Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                        
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal Command Not Found Error occured in execution of {ctx.command}')
                        logger.debug(f"[ERROR] {ctx.command} | {error}")  

        #CHECK FAILURE

                elif isinstance(error, commands.CheckFailure):
                        embed = discord.Embed(title = f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal Check Failure Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                                
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal Check Failure Error occured in execution of {ctx.command}')
                        logger.debug(f"[ERROR] {ctx.command} | {error}")

                #CHECK ANY FAILURE

                elif isinstance(error, commands.CheckAnyFailure):
                        embed = discord.Embed(title = f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal Check Any Failure Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                        
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal Check Any Failure Error occured in execution of {ctx.command}')
                        logger.debug(f"[ERROR] {ctx.command} | {error}")              

                #PRIVATE MESSAGE ONLY

                elif isinstance(error, commands.PrivateMessageOnly):
                        embed = discord.Embed(title = f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal Private Message Only Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                        
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal Private Message Only Error occured in execution of {ctx.command}')
                        logger.debug(f"[ERROR] {ctx.command} | {error}")      

                #NO PRIVATE MESSAGE

                elif isinstance(error, commands.NoPrivateMessage):
                        embed = discord.Embed(title = f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal No Private Message Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                        
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal No Private Message Error occured in execution of {ctx.command}')
                        logger.debug(f"[ERROR] {ctx.command} | {error}")      

                #NOT OWNER

                elif isinstance(error, commands.NotOwner):
                        embed = discord.Embed(title = f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal Not Owner Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                        
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal Not Owner Error occured in execution of {ctx.command}')
                        logger.debug(f"[ERROR] {ctx.command} | {error}")      

                #MISSING PERMISSIONS

                elif isinstance(error, commands.MissingPermissions):
                        embed = discord.Embed(title = f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal Missing Permissions Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                        
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal Missing Permissions Error occured in execution of {ctx.command}')
                        logger.debug(f"[ERROR] {ctx.command} | {error}")      
                
                #MISSING ROLE

                elif isinstance(error, commands.MissingRole):
                        embed = discord.Embed(title = f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal Missing Role Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                        
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal Missing Role Error occured in execution of {ctx.command}')
                        logger.debug(f"[ERROR] {ctx.command} | {error}")      

                #BOT MISSING ROLE

                elif isinstance(error, commands.BotMissingRole):
                        embed = discord.Embed(title = f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal Bot Missing Role Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                        
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal Bot Missing Role Error occured in execution of {ctx.command}')
                        logger.debug(f"[ERROR] {ctx.command} | {error}")      

                #MISSING ANY ROLE

                elif isinstance(error, commands.MissingAnyRole):
                        embed = discord.Embed(title = f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal Missing Any Role Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                        
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal Missing Any Role Error occured in execution of {ctx.command}')
                        logger.debug(f"[ERROR] {ctx.command} | {error}")      

                #BOT MISSING ANY ROLE

                elif isinstance(error, commands.BotMissingAnyRole):
                        embed = discord.Embed(title = f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal Bot Missing Any Role Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                        
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal Bot Missing Any Role Error occured in execution of {ctx.command}')
                        logger.debug(f"[ERROR] {ctx.command} | {error}")   

                #NSFW CHANNEL REQUIRED

                elif isinstance(error, commands.NSFWChannelRequired):
                        embed = discord.Embed(title = f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal NSFW Channel Required Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                        
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal NSFW Channel Required Error occured in execution of {ctx.command}')
                        logger.debug(f"[ERROR] {ctx.command} | {error}")      
   
                #DISABLED COMMAND

                elif isinstance(error, commands.DisabledCommand):
                        embed = discord.Embed(title = f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal Disabled Command Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                        
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal Disabled Command Error occured in execution of {ctx.command}')
                        logger.debug(f"[ERROR] {ctx.command} | {error}")  

                #COMMAND INVOKE ERROR

                elif isinstance(error, commands.CommandInvokeError):
                        embed = discord.Embed(title = f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal Command Invoke Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                        
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal Command Invoke Error occured in execution of {ctx.command}')
                        logger.debug(f"[ERROR] {ctx.command} | {error}")  

                #COMMAND ON COOLDOWN

                elif isinstance(error, commands.CommandOnCooldown):
                        embed = discord.Embed(title = f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal Command On Cooldown Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                        
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal Command On Cooldown Error occured in execution of {ctx.command}')
                        logger.debug(f"[ERROR] {ctx.command} | {error}")  

                #MAX CONCURRENCY REACHED    

                elif isinstance(error, commands.MaxConcurrencyReached):
                        embed = discord.Embed(title = f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal Max Concurrency Reached Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                        
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal Max Concurrency Reached Error occured in execution of {ctx.command}')
                        logger.debug(f"[ERROR] {ctx.command} | {error}")                     

        #EXTENSION ERROR

                elif isinstance(error, commands.ExtensionError):
                        embed = discord.Embed(title = f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal EXT Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                        
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal Extension Error occured in execution of {ctx.command}')
                        logger.debug(f"[ERROR] {ctx.command} | {error}")


                #EXTENSION ALREADY LOADED

                elif isinstance(error, commands.ExtensionAlreadyLoaded):
                        embed = discord.Embed(title = f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal EXT Already Loaded Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                        
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal Extension Already Loaded Error occured in execution of {ctx.command}')
                        logger.debug(f"[ERROR] {ctx.command} | {error}")

                #EXTENSION NOT LOADED

                elif isinstance(error, commands.ExtensionNotLoaded):
                        embed = discord.Embed(title = f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal EXT Not Loaded Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                        
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal Extension Not Loaded Error occured in execution of {ctx.command}')
                        logger.debug(f"[ERROR] {ctx.command} | {error}")

                #NO ENTRY POINT ERROR

                elif isinstance(error, commands.NoEntryPointError):
                        embed = discord.Embed(title = f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal No Entry Point Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                        
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal No Entrypoint Error occured in execution of {ctx.command}')
                        logger.debug(f"[ERROR] {ctx.command} | {error}")

                #EXTENSION FAILED

                elif isinstance(error, commands.ExtensionFailed):
                        embed = discord.Embed(title = f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal EXT Failed Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                        
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal Extension Failed Error occured in execution of {ctx.command}')
                        logger.debug(f"[ERROR] {ctx.command} | {error}")

                #EXTENSION NOT FOUND

                elif isinstance(error, commands.ExtensionNotFound):
                        embed = discord.Embed(title = f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal EXT Not Found Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                        
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal Extension Not Found Error occured in execution of {ctx.command}')
                        logger.debug(f"[ERROR] {ctx.command} | {error}")

        #CLIENT EXCEPTION

                #COMMAND REGISTRATION ERROR

                elif isinstance(error, commands.CommandRegistrationError):
                        embed = discord.Embed(title = f"Type = `Fatal`",color=0x9B59B6, timestamp=ctx.message.created_at)

                        embed.set_author(name="IVRY Error", icon_url=self.client.user.avatar_url)
                        embed.add_field(name = "Error", value="`Internal Command Registration Error`", inline=True)
                        embed.add_field(name = "Error Point", value=f"`{ctx.command}`", inline=True)
                        embed.add_field(name = "Trace Back", value=f"```CSS\n{error}```", inline=False)
                        embed.set_footer(text=f"{config.version} | {config.shards}")
                        
                        await ctx.send(embed=embed)
                        print(f'[WARNING] A Fatal internal Command Registration Error occured in execution of {ctx.command}')
                        logger.debug(f"[ERROR] {ctx.command} | {error}")
                
                else:
                        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
                        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)  

def setup(client):
    client.add_cog(Errors(client))