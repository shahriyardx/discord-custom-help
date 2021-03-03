from discord.ext import commands

class Co(commands.Cog):
    """Some help for CO"""

    def __init__(self, bot):
        self.bot = bot
    

    @commands.command()
    async def test(self, ctx):
        """A test command"""
        await ctx.send("Test")
    

def setup(bot):
    bot.add_cog(Co(bot))