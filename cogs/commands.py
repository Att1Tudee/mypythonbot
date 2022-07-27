import pymongo
from pymongo import MongoClient
import discord
import time
import datetime
import motor.motor_asyncio as motor
from discord.ext import commands

client= motor.AsyncIOMotorClient("mongodb+srv://bot:bot@cluster0.x3vrg.mongodb.net/data")

db = client["data"]
collection = db["motds"]
timedb = db["time"]

class Commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        with open("discordchannelid.txt", "r") as f:
            self.discordchannelid=int(f.read())
    token = open("token.txt", "r").read()

    @commands.Cog.listener()
    async def on_ready(self):
        print('Commands is online.')

# Post random line

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def randpost(self, ctx):
                randness = collection.aggregate([{'$sample': {'size': 1 }}])
                async for result in randness:
                                print("Requested random post from database:", result["motd"])
                                embed = discord.Embed(description=f"```yaml\nMessage of the day:\n{result['motd']}\n```", color=discord.Color.blue())
                                await ctx.send(embed=embed)

# Set time into database

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def settimee(self, ctx, *, timee):
                embed = discord.Embed(description=f"```yaml\nSetting this post time:\n{timee}\n```", color=discord.Color.blue())
                timedb.delete_many({})
                time.sleep(5)
                newvalue = {"time":str(timee)}
                timedb.insert_one(newvalue)
                await ctx.send(embed=embed)
                print("This time set in database:", timee)   
                
#   View UTC time

    @commands.command()
    async def viewutctime(self, ctx):
        x = datetime.datetime.utcnow()
        y = (x.strftime("%H:%M:%S"))
        embed= discord.Embed(description=f"```fix\nCurrent time in UTC is \n{y}\n```", color=discord.Color.blue())
        await ctx.send(embed=embed)

# Find time from database and post it                                                           

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def viewpostingtime(self, ctx):
                findtimeh = timedb.find({}, { "time": 1 })
                async for result in findtimeh:
                            print("Found current time from database:", result["time"])
                            embed = discord.Embed(description=f"```yaml\nCurrent posting time in UTC is:\n{result['time']}\n```", color=discord.Color.blue())
                            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Commands(bot))
