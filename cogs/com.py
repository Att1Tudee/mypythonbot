import discord
import os
import random
import datetime
from discord.ext import commands, tasks

class Com(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        with open("discordchannelid.txt", "r") as f:
            self.discordchannelid=int(f.read())
    token = open("token.txt", "r").read()

    @commands.Cog.listener()
    async def on_ready(self):
        print('Commands is online.')

    # Post current time as utcnow(THIS WORKS EVERYWHERE)

    @commands.command()
    async def viewutctime(self, ctx):
        x = datetime.datetime.utcnow()
        y = (x.strftime("%H:%M:%S"))
        embed= discord.Embed(description=f"```fix\nCurrent time in UTC is \n{y}\n```", color=discord.Color.blue())
        await ctx.send(embed=embed)


    # Request Ping

    @commands.command()
    async def ping(self, ctx):
            print ('Ping requested')
            await ctx.send(f'Ping is {round(self.bot.latency * 1000)}ms')

    @commands.command(name="setchannel")
    @commands.has_permissions(manage_roles=True)
    async def setchannel(self, ctx):

        channel = ctx.channel
        x = (str(channel.id))
        print("Setting bot channel to", x)
        f=open ('discordchannelid.txt', 'w')
        f.seek (0, 0)
        f.write(x)
        f.close()


    


def setup(bot):
    bot.add_cog(Com(bot))
