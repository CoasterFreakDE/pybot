import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')


def caps_pls(text):
    return text.upper()


@bot.command()
async def say(ctx, *, arg):
    await ctx.send(arg)


@say.error
async def say_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Bitte gebe an, was ich sagen soll.')


@bot.command()
async def caps(ctx, *, arg: caps_pls):
    await ctx.send(arg)


@caps.error
async def caps_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Bitte gebe an, was ich schreien soll.')


@bot.command()
async def kill(ctx, member: discord.Member):
    await ctx.send(f'{member.display_name} wurde gekillt.')


@kill.error
async def kill_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('Ich kann ihn nicht finden sry.')


bot.run('')
