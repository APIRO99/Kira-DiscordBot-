import discord
from discord.ext import commands
import random

class general(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    
    @commands.command(name='ping', aliases=['p'])
    async def ping(self, ctx):
        await ctx.send("Pong! :ping_pong:")

    
    """Adds two numbers together."""
    @commands.command()
    async def add(self, ctx, left: int, right: int):
        await ctx.send(left + right)


    """Rolls a dice in NdN format."""
    @commands.command()
    async def roll(self, ctx, dice: str):
        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await ctx.send('Format has to be in NdN!')
            return

        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await ctx.send(result)


    """Chooses between multiple choices."""
    @commands.command()
    async def choose(self, ctx, *choices: str):
        await ctx.send(random.choice(choices))


    """Repeats a message multiple times."""
    @commands.command()
    async def repeat(self, ctx, times: int, content='repeating...'):
        for i in range(times):
            await ctx.send(content)


    """Says when a member joined."""
    @commands.command()
    async def joined(self, ctx, member: discord.Member):
        await ctx.send('{0.name} joined in {0.joined_at}'.format(member))


    def setup(bot):
        bot.add_cog(general(bot))