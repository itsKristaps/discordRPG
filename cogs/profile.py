from discord import app_commands
from discord.ext import commands


class Profile(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="start",
        description="Create your profile"
    )
    async def start(self, interaction):
        await interaction.response.send_message(
            f"Welcome {interaction.user.mention}! hello monkey"
        )


async def setup(bot):
    await bot.add_cog(Profile(bot))