from discord.ext import commands

class Co2(commands.Cog):
    """Some help for CO2"""

    def __init__(self, bot):
        self.bot = bot
    

    @commands.group()
    async def lest(self, ctx):
        """A test command"""
        await ctx.send("Lest")
    
    @lest.command()
    async def dest(self, ctx):
        await ctx.send("Dest")

def setup(bot):
    bot.add_cog(Co2(bot))