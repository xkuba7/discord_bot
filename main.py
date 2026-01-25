import discord
from dotenv import load_dotenv
import os
from discord.ext import commands

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)

@bot.tree.command(name="ping", description="check if bot is alive")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong")

@bot.tree.command(name="parrot", description="repeats argument")
async def parrot(interaction: discord.Interaction, message: str):
    await interaction.response.send_message(message)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print("Command tree synced")

print("Local commands:", bot.tree.get_commands())
token = str(os.getenv("DISCORD_TOKEN"))
bot.run(token)
