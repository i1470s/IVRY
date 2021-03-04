#PRIMARY IMPORTS

import base64, binascii, codecs, discord, logging

#SECONDARY IMPORTS

from io import BytesIO
from discord.ext import commands
from discord.ext.commands.errors import BadArgument
from data import config 
from extras import http

#LOGGING

logger = logging.getLogger("ivry")
logger.debug("misc.py Started")

class Misc(commands.Cog):
    def __init__(self, client):
        self.client = client

    #ENCODER

    @commands.group()
    async def encode(self, ctx):
        if ctx.invoked_subcommand is None:
                embed = discord.Embed(color=0x9B59B6)

                embed.set_author(name="IVRY Encrypt", icon_url=self.client.user.avatar_url)
                embed.add_field(name = "Avalible Encoders", value=f"\n `base32`- UTF-8 \n `base64`- UTF-8 \n `base85`- UTF-8 \n `rot13`- UTF-8 \n `hex`- UTF-8 \n `ascii85`- UTF-8", inline=True)
                embed.set_footer(text=f"{config.version} | {config.shards}")
                await ctx.send(embed=embed)

    #DECODER

    @commands.group()
    async def decode(self, ctx):
        if ctx.invoked_subcommand is None:
                embed = discord.Embed(color=0x9B59B6)

                embed.set_author(name="IVRY Encrypt", icon_url=self.client.user.avatar_url)
                embed.add_field(name = "Avalible Decoders", value=f"\n `base32`- UTF-8 \n `base64`- UTF-8 \n `base85`- UTF-8 \n `rot13`- UTF-8 \n `hex`- UTF-8 \n `ascii85`- UTF-8", inline=True)
                embed.set_footer(text=f"{config.version} | {config.shards}")
                await ctx.send(embed=embed)

    #DETECT FILE

    async def detect_file(self, ctx):
        if ctx.message.attachments:
            file = ctx.message.attachments[0].url

            if not file.endswith(".txt"):
                raise BadArgument(".txt files only")

        try:
            content = await http.get(file, no_cache=True)
        except Exception:
            raise BadArgument("Invalid .txt file")

        if not content:
            raise BadArgument("File you've provided is empty")
        return content

    #ENCRYPTER

    async def encryptout(self, ctx, convert: str, input):
        if not input:
            return await ctx.send(f"Aren't you going to give me anything to encode/decode **{ctx.author.name}**")

        async with ctx.channel.typing():
            if len(input) > 1900:
                try:
                    data = BytesIO(input.encode('utf-8'))
                except AttributeError:
                    data = BytesIO(input)

                try:
                    return await ctx.send(
                        content=f"📑 **{convert}**",
                        file=discord.File(data, filename=("Encryption"))
                    )
                except discord.HTTPException:
                    return await ctx.send(f"The file I returned was over 8 MB, sorry {ctx.author.name}...")

            try:
                await ctx.send(f"📑 **{convert}**```fix\n{input.decode('UTF-8')}```")
            except AttributeError:
                await ctx.send(f"📑 **{convert}**```fix\n{input}```")

    #BASE 32 SUB COMMAND

    @encode.command(name="base32", aliases=["b32"])
    async def encode_base32(self, ctx, *, input: commands.clean_content = None):
        if not input:
            input = await self.detect_file(ctx)

        await self.encryptout(
            ctx, "Text -> base32", base64.b32encode(input.encode('UTF-8'))
        )

    @decode.command(name="base32", aliases=["b32"])
    async def decode_base32(self, ctx, *, input: commands.clean_content = None):
        if not input:
            input = await self.detect_file(ctx)

        try:
            await self.encryptout(ctx, "base32 -> Text", base64.b32decode(input.encode('UTF-8')))
        except Exception:
            await ctx.send("Invalid base32...")

    #BASE 64 SUB COMMAND

    @encode.command(name="base64", aliases=["b64"])
    async def encode_base64(self, ctx, *, input: commands.clean_content = None):
        if not input:
            input = await self.detect_file(ctx)

        await self.encryptout(
            ctx, "Text -> base64", base64.urlsafe_b64encode(input.encode('UTF-8'))
        )

    @decode.command(name="base64", aliases=["b64"])
    async def decode_base64(self, ctx, *, input: commands.clean_content = None):
        if not input:
            input = await self.detect_file(ctx)

        try:
            await self.encryptout(ctx, "base64 -> Text", base64.urlsafe_b64decode(input.encode('UTF-8')))
        except Exception:
            await ctx.send("Invalid base64...")

    #ROT 13 SUB COMMAND

    @encode.command(name="rot13", aliases=["r13"])
    async def encode_rot13(self, ctx, *, input: commands.clean_content = None):
        if not input:
            input = await self.detect_file(ctx)

        await self.encryptout(
            ctx, "Text -> rot13", codecs.decode(input, 'rot_13')
        )

    @decode.command(name="rot13", aliases=["r13"])
    async def decode_rot13(self, ctx, *, input: commands.clean_content = None):
        if not input:
            input = await self.detect_file(ctx)

        try:
            await self.encryptout(ctx, "rot13 -> Text", codecs.decode(input, 'rot_13'))
        except Exception:
            await ctx.send("Invalid rot13...")

    #HEX SUB COMMAND

    @encode.command(name="hex")
    async def encode_hex(self, ctx, *, input: commands.clean_content = None):
        if not input:
            input = await self.detect_file(ctx)

        await self.encryptout(
            ctx, "Text -> hex", binascii.hexlify(input.encode('UTF-8'))
        )

    @decode.command(name="hex")
    async def decode_hex(self, ctx, *, input: commands.clean_content = None):
        if not input:
            input = await self.detect_file(ctx)

        try:
            await self.encryptout(ctx, "hex -> Text", binascii.unhexlify(input.encode('UTF-8')))
        except Exception:
            await ctx.send("Invalid hex...")

    #BASE 85 SUB COMMAND

    @encode.command(name="base85", aliases=["b85"])
    async def encode_base85(self, ctx, *, input: commands.clean_content = None):
        if not input:
            input = await self.detect_file(ctx)

        await self.encryptout(
            ctx, "Text -> base85", base64.b85encode(input.encode('UTF-8'))
        )

    @decode.command(name="base85", aliases=["b85"])
    async def decode_base85(self, ctx, *, input: commands.clean_content = None):
        if not input:
            input = await self.detect_file(ctx)

        try:
            await self.encryptout(ctx, "base85 -> Text", base64.b85decode(input.encode('UTF-8')))
        except Exception:
            await ctx.send("Invalid base85...")

    #ASCII 85 SUB COMMAND

    @encode.command(name="ascii85", aliases=["a85"])
    async def encode_ascii85(self, ctx, *, input: commands.clean_content = None):
        if not input:
            input = await self.detect_file(ctx)

        await self.encryptout(
            ctx, "Text -> ASCII85", base64.a85encode(input.encode('UTF-8'))
        )

    @decode.command(name="ascii85", aliases=["a85"])
    async def decode_ascii85(self, ctx, *, input: commands.clean_content = None):
        if not input:
            input = await self.detect_file(ctx)

        try:
            await self.encryptout(ctx, "ASCII85 -> Text", base64.a85decode(input.encode('UTF-8')))
        except Exception:
            await ctx.send("Invalid ASCII85...")


def setup(client):
    client.add_cog(Misc(client))
