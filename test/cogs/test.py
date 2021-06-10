from discord.ext import commands


class Test(commands.Cog):
    """A test cog description"""
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command()
    async def test(self, ctx) -> None:
        """A test command of test cog"""
        await ctx.send("Test message from test command")


def setup(bot):
    bot.add_cog(Test(bot))