import discord
import asyncio
import os
import random
import datetime
import motor.motor_asyncio as motor
from discord.ext import commands, tasks


client= motor.AsyncIOMotorClient("mongodb+srv://bot:bot@cluster0.x3vrg.mongodb.net/data")

db = client["data"]
collection = db["motds"]
guildss = db["guilds"]
timedb = db["time"]

class Tehloop(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        with open("discordchannelid.txt", "r") as f:
            self.discordchannelid=int(f.read())

    @commands.Cog.listener()
    async def on_ready(self):
        print('tehloop is online.')
        self.called_once_a_day.start()
   

#       Message timing check loop

    @tasks.loop(seconds=1)
    async def called_once_a_day(self):
        self.target_channel = self.bot.get_channel(self.discordchannelid)
        x = datetime.datetime.utcnow()
        y = (x.strftime("%H:%M:%S"))
        z = open("postingtime.txt", "r").read()
        if y == z.strip():
           randness = collection.aggregate([{'$sample': {'size': 1 }}])
           async for result in randness:
                            print("Requested random post from database:", result["motd"])
                            embed = discord.Embed(description=f"```yaml\nMessage of the day:\n{result['motd']}\n```", color=discord.Color.blue())
                            await self.target_channel.send(embed=embed)
                       
    @called_once_a_day.before_loop
    async def before(self):
        await self.bot.wait_until_ready()
        print("Finished waiting")



def setup(bot):
    bot.add_cog(Tehloop(bot))
