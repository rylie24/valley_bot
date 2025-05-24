import discord

from discord.ext import commands

class Player(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name="create_player")
    async def create_player(self, interaction: discord.Interaction):
        await interaction.response.send_message("Player command executed!")
        await interaction.followup.send("This is a follow-up message!")

async def setup(bot: commands.Bot):
    await bot.add_cog(Player(bot))