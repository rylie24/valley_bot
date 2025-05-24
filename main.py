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

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("🚫 You can only use this command in approved channels.")

    async def setup_hook(self):
        # Load cogs
        for cog in cogs:
            try:
                await self.load_extension(cog)
                await self.tree.sync()
            except Exception as e:
                print(f"Failed to load {cog}: {e}")

        @self.check
        async def global_channel_check(interaction: discord.Interaction):
            if interaction.channel.id != 1374982862121598986:
                await interaction.response.send_message(
                    "This command can only be used in the designated channel.", ephemeral=True
                )
                return False

bot = ValleyBot()
bot.run(TOKEN)