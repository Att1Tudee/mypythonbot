import logging
import discord
import os
import datetime
from discord.ext import commands, tasks


bot = commands.Bot(command_prefix="!")
bot.remove_command('help')
token = open("token.txt", "r").read()

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit=amount)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    print('Loaded cog')

@bot.command()
@commands.has_permissions(manage_messages=True)
async def unload(ctx, extension):
    print('Unloaded cog')
    bot.unload_extension(f'cogs.{extension}')

@bot.command()
@commands.has_permissions(manage_messages=True)
async def re(ctx, extension):
    print('Reloaded cog')
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')

for filename in os.listdir('cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

# Make bot like everyone can put their own tips inside, including author of the tip(CURRENTLY IT ADDS THE AUTHOR VALUE BUT DOESN'T POST IT)
# Channelid directly into the database by requesting !setchannel, and unsetchannel too
# Create Switchtip,(allow this done twice) change last tip sent into next via editing the message(by reaction), not posting new
# Have an addon that has currently online helpers listed in same embed, ask for people who are willing to join in that list(propably a role reaction bot with embed)
# Figure out how to set bot post in specific channel without the extra file(discordchannelid)
# Make channel strict that only at specific channel the commands can work, not anything else
# ERROR HANDLING
# Roll cmd or similar to change tip if it was too early to post same tip again, for example via react
# Make customstatus roll each 30seconds
# Figure out how to check database with loop less than each second lol(CURRENTLY WORKING FROM FILE)
# Sort the fuqn one-by-one tiplist, SOMETHIGN WITH PAGINATION
# alphabetical order for database request



bot.run(token)
