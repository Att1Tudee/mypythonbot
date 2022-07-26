import pymongo
from pymongo import MongoClient
import discord
import os
import time
import disputils
from disputils import BotEmbedPaginator, BotConfirmation, BotMultipleChoice
import motor.motor_asyncio as motor
import random
from discord.ext import commands, tasks

client= motor.AsyncIOMotorClient("mongodb+srv://bot:bot@cluster0.x3vrg.mongodb.net/data")

db = client["data"]
collection = db["motds"]
guildss = db["guilds"]
timedb = db["time"]

class Mongocmd(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        with open("discordchannelid.txt", "r") as f:
            self.discordchannelid=int(f.read())
    token = open("token.txt", "r").read()

    @commands.Cog.listener()
    async def on_ready(self):
        print('Mongocmd is online.')

#       Adding a line into the database

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def addline(self, ctx, *, lineee):
                embed = discord.Embed(description=f"```yaml\nAdded this motd in database:\n{lineee}\n```", color=discord.Color.blue())
                post = {"motd":str(lineee), "author":ctx.message.author.name}
                collection.insert_one(post)
                await ctx.send(embed=embed)
                print("Added this line in database:", lineee)

#       Find a specific line from database

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def findline(self, ctx, *, findthispls):
                myquery = {"motd": { "$regex": "^" + findthispls} }
                findpost = collection.find(myquery, {"author": 1,"motd":1})
                async for result in findpost:
                            print("Requested this motd from database:", findthispls)
                            print("Found requested motd from database:", result["motd"])
                            embed = discord.Embed(description=f"```yaml\nFound this motd from database:\n{result['motd']}\n```", color=discord.Color.blue())
                            await ctx.send(embed=embed)

#      Request data in a file

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def requestdata(self, ctx):
                print("Requested data into dbstorage.txt")
                ssslsst = []
              
                async for result in collection.find({}):
                            ssslsst = str([result["writeup"]]).strip("[]'").replace('"','')
                                                       
                            f=open ('dbstorage.txt', 'a')
                            f.seek (0, 0)                            
                            f.write(ssslsst + "\n\n")                          
                            f.close()
                            
#       Show data from file

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def showdata(self, ctx):
        print("Requested showdata")
        with open ("dbstorage.txt") as f:
                            text = f.read()          
                            embed = discord.Embed(description=f"```fix\n{text}```", color=discord.Color.blue())
                            await ctx.send(embed=embed)
                            f=open ("dbstorage.txt", 'w')                           
                            f.close
 
#                   Delete line

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def deleteline(self, ctx, *, deletepostedline):
                goodbye = collection.find({"motd":deletepostedline})
                async for result in goodbye:
                                print("Requested this motd from database for it to be deleted:", deletepostedline)
                                print("Found requested motd from database and deleting it:", result["motd"])
                                embed = discord.Embed(description=f"```yaml\nFound this motd from database and deleted it:\n{result['motd']}\n```", color=discord.Color.blue())
                                await ctx.send(embed=embed)
                farewell = await collection.delete_one({"motd":deletepostedline})

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
                

# Find time from database and post it(viewcurrenttime) LOL how this actually is done                                                           

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def v(self, ctx):
                findtimeh = timedb.aggregate([{'$sample': {'size': 1 }}])
                async for result in findtimeh:
                            print("Found current time from database:", result["time"])
                            embed = discord.Embed(description=f"```yaml\nCurrent posting time in UTC is:\n{result['time']}\n```", color=discord.Color.blue())
                            await ctx.send(embed=embed)
               

  #                      async for y in collection.find({},{ "_id": 0, "time": 1})

# Get channel ID that should be used(checking duplicate doesn't work)
    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def usethischannel(self,ctx, *, chanid):
            for guild in self.bot.guilds:
                x = guild.id
                y = collection.find_one(x)
                print(y)
                if y == x:
                    print("Guild already exist")
            else:
                createguild = {"guildid":x ,"channel":chanid}
                guildss.insert_one(createguild)
                print ("guild id:", x,"guild channel:", chanid)

#               Testing on usethistime getting from db

@commands.command()
async def embedpages(self):
    page1 = discord.Embed (
        title = 'Page 1/3',
        description = 'Description',
        colour = discord.Colour.orange()
    )
    page2 = discord.Embed (
        title = 'Page 2/3',
        description = 'Description',
        colour = discord.Colour.orange()
    )
    page3 = discord.Embed (
        title = 'Page 3/3',
        description = 'Description',
        colour = discord.Colour.orange()
    )

    pages = [page1, page2, page3]

    message = await client.say(embed = page1)

    await client.add_reaction(message, '⏮')
    await client.add_reaction(message, '◀')
    await client.add_reaction(message, '▶')
    await client.add_reaction(message, '⏭')

    i = 0
    emoji = ''

    while True:
        if emoji == '⏮':
            i = 0
            await client.edit_message(message, embed = pages[i])
        elif emoji == '◀':
            if i > 0:
                i -= 1
                await client.edit_message(message, embed = pages[i])
        elif emoji == '▶':
            if i < 2:
                i += 1
                await client.edit_message(message, embed = pages[i])
        elif emoji == '⏭':
            i = 2
            await client.edit_message(message, embed=pages[i])
        
        res = await client.wait_for_reaction(message = message, timeout = 30.0)
        if res == None:
            break
        if str(res[1]) != 'Tips at server local#8703':  #Example: 'MyBot#1111'
            emoji = str(res[0].emoji)
            await client.remove_reaction(message, res[0].emoji, res[1])

    await client.clear_reactions(message)    



def setup(bot):
    bot.add_cog(Mongocmd(bot))
