from discord.ext import commands
import os

class TestBot(commands.Bot):
    """A test bot"""
    def __init__(self, **options):
        super().__init__(**options)

    async def on_ready(self):
        self.load_extension('cogs.test')
        self.load_extension('dch')

        print("Test bot is ready")
    
    async def on_message(self, message):
        await self.process_commands(message)
    

# Setting environment vars
os.environ['DCH_COLOR'] = 'ffffff'

bot = TestBot(command_prefix='..')
bot.run('TOKEN')