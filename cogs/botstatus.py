import discord
from discord.ext import commands

class Botstatus(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Botstatus is online.')

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def dnd(self, ctx):
        print ('Botpresence changed to Do Not Disturb')
        await self.bot.change_presence(status=discord.Status.dnd)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def dndwatching(self, ctx, *, status: str):
        print ('Botpresence changed to Do Not Disturb, Watching', status)
        await self.bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name=status))

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def dndlisteningto(self, ctx, *, status: str):
        print ('Botpresence changed to Do Not Disturb, Listening to', status)
        await self.bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.listening, name=status))

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def idle(self, ctx):
        print ('Botpresence changed to Idle')
        await self.bot.change_presence(status=discord.Status.idle)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def idlewatching(self, ctx, *, status: str):
        print ('Botpresence changed to Idle, Watching', status)
        await self.bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name=status))


    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def idlelisteningto(self, ctx, *, status: str):
        print ('Botpresence changed to Idle, Listening to', status)
        await self.bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.listening, name=status))

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def online(self, ctx):
        print ('Botpresence changed to Online')
        await self.bot.change_presence(status=discord.Status.online)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def onlinewatching(self, ctx, *, status: str):
        print ('Botpresence changed to Online, Watching', status)
        await self.bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=status))

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def onlinelisteningto(self, ctx, *, status: str):
        print ('Botpresence changed to online, Listening to', status)
        await self.bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name=status))

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def playing(self, ctx, *, status: str):
        print ('Botpresence changed to Playing', status),
        await self.bot.change_presence(activity=discord.Game(name=status))

def setup(bot):
    bot.add_cog(Botstatus(bot))
