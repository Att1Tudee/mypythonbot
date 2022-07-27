import discord
import datetime
import motor.motor_asyncio as motor
from discord.ext import commands, tasks

client= motor.AsyncIOMotorClient("mongodb+srv://bot:bot@cluster0.x3vrg.mongodb.net/data")

# variables

db = client["data"]
collection = db["motds"]
timedb = db["time"]
updateintervalfordatabasecheckinminutes = 1

# give random value for variable that changes in time check

timeindatabase = "00:00:00"

class Tasks(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        with open("discordchannelid.txt", "r") as f:
            self.discordchannelid=int(f.read())
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Tasks is online.')
        self.called_once_a_day.start()
        self.dbtimechecker.start()

#   Check database time and set it into variable
                      
    @tasks.loop(minutes=updateintervalfordatabasecheckinminutes)
    async def dbtimechecker(self):
        try:
            dbtimecheckerresult = timedb.find({}, { "time": 1 })
            async for result in dbtimecheckerresult:
                global timeindatabase
                timeindatabase = result["time"]
                print ("Time set in database:", timeindatabase)
            
        except Exception as e:
            print(e)     
            
#       Message timing check loop, if the time matches in current UTC, post executes

    @tasks.loop(seconds=1)
    async def called_once_a_day(self):
        global timeindatabase
        self.target_channel = self.bot.get_channel(self.discordchannelid)
        x = datetime.datetime.utcnow()
        y = (x.strftime("%H:%M:%S"))        
        z = timeindatabase
        if y == z.strip():
           randness = collection.aggregate([{'$sample': {'size': 1 }}])
           async for result in randness:
                            print("Requested random post from database:", result["motd"])
                            embed = discord.Embed(description=f"```yaml\nMessage of the day:\n{result['motd']}\n```", color=discord.Color.blue())
                            await self.target_channel.send(embed=embed)
                            
def setup(bot):
    bot.add_cog(Tasks(bot))
