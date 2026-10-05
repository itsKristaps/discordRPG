import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True


class MyBot(commands.Bot):
    async def setup_hook(self):
        await self.load_extension("cogs.profile")
        await self.tree.sync()


class MyBot(commands.Bot):
    async def setup_hook(self):
        print("Loading profile cog...")

        await self.load_extension("cogs.profile")

        print("Syncing commands...")

        synced = await self.tree.sync()

        print(f"Synced {len(synced)} commands")


bot = MyBot(
    command_prefix="!",
    intents=intents
)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    print(f"Test print")


bot.run(TOKEN)