import discord
import os

from discord.ext import commands
from cogs.general import general
from cogs.minecraftServer import MinecraftServerManager

from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='{0} '.format(os.getenv('BOT_PREFIX')),intents=intents)

bot.add_cog(general(bot))
bot.add_cog(MinecraftServerManager(bot))

@bot.event
async def on_ready():
    print('--------------------')
    print('Logged in as')
    print("{0} - {1}".format(bot.user.name, bot.user.id))
    print('--------------------')

bot.run(os.getenv('BOT_TOKEN'))