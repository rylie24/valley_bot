import discord
from discord.ext import commands

from src.config import TOKEN

cogs = [
    "src.player",
]

class ValleyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="~", intents=discord.Intents.all())

    async def on_ready(self):
        print(f"Logged in as {self.user.name}")
        print("------")

    async def setup_hook(self):
        # Load cogs
        for cog in cogs:
            try:
                await self.load_extension(cog)
                await self.tree.sync()
            except Exception as e:
                print(f"Failed to load {cog}: {e}")


bot = ValleyBot()
bot.run(TOKEN)