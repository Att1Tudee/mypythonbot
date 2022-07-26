import discord
from discord.ext import commands

class Helpfile(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        with open("discordchannelid.txt", "r") as f:
            self.discordchannelid=int(f.read())

    @commands.Cog.listener()
    async def on_ready(self):
        print('Helpfile is online.')

    @commands.Cog.listener()
    async def on_message(self,message):
        self.target_channel = self.bot.get_channel(self.discordchannelid)
        if message.content.startswith('!help'):
            embedVar = discord.Embed(title="```You must have manage_messages permission to use these commands.\n Bot status can be Watching, Listening to or Playing,\n but sadly not custom. It's limited like that.```", description=" ", color=discord.Color(0x000000))
            embedVar.add_field(name="!viewutctime", value="View current time in UTC.", inline=False)
            embedVar.add_field(name="!addline", value="Add a line in database", inline=False)
            embedVar.add_field(name="!findline", value="Find a line that stars with the first word you know(case sensitive)", inline=False)
            embedVar.add_field(name="!requestdata", value="Need to do this before !showdata", inline=False)
            embedVar.add_field(name="!showdata", value="Shows every line in one post from database. Note you must do !requestdata first", inline=False)
            embedVar.add_field(name="!deleteline", value="Deletes a line from database. Note you must write the line exactly as shown from database.", inline=False)
            embedVar.add_field(name="!dnd, !idle, !online ", value="Sets bot status into Do Not Disturb, Idle or Online", inline=False)
            embedVar.add_field(name="!dndwatching, !idlewatching, !onlinewatching", value="DnD, Idle or Online status with Watching in front, and your own sentence after.\n For example, Watching a movie.", inline=False)
            embedVar.add_field(name="!dndlisteningto !idlelisteningto !onlinelisteningto", value="Same statuses with Listening to", inline=False)
            embedVar.add_field(name="!playing", value="Status with Playing in front of your sentence.", inline=False)
            await self.target_channel.send(embed=embedVar)


@commands.Cog.listener()
async def on_message(self,message):
    self.target_channel = self.bot.get_channel(self.discordchannelid)




def setup(bot):
    bot.add_cog(Helpfile(bot))
