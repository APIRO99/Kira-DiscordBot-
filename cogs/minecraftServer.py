from discord.ext import commands
import requests
import json
import os

_api = os.getenv('AWSMINECRAFTAPI')

# For authorization, you can use either your bot token 
_headers = {
  "Authorization": "Bot {0}".format(os.getenv('BOT_TOKEN'))
}

class MinecraftServerManager(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  def turnOffServer(self):
    response = requests.post(_api + '/turnoff', headers=_headers)
    json_data = json.loads(response.text)
    print(json_data)
    return json_data['msg']

  def turnOnServer(self):
    response = requests.post(_api + '/turnon', headers=_headers)
    json_data = json.loads(response.text)
    print(json_data)
    return json_data['msg']


  @commands.command()
  async def TurnOffServer(self, ctx):
    if ctx.author == self.bot.user: return
    res = self.turnOffServer();
    await ctx.send(res)

  @commands.command()
  async def TurnOnServer(self, ctx):
    if ctx.author == self.bot.user: return
    res = self.turnOnServer();
    await ctx.send(res)


  def setup(bot):
    self.bot.add_cog(MinecraftServerManager(self.bot))