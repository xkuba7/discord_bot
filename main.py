import discord
from dotenv import load_dotenv
import os
from discord.ext import commands

import data_updater

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)

@bot.tree.command(name="ping", description="check if bot is alive")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong")

@bot.tree.command(name="ping_user", description="ping a user")
async def ping_user(interaction: discord.Interaction, user: discord.User):
    await interaction.response.send_message(f"Hey {user.mention}")

@bot.tree.command(name="parrot", description="repeats argument")
async def parrot(interaction: discord.Interaction, message: str):
    await interaction.response.send_message(message)

@bot.tree.command(name="join_leaderboard", description="allows a user to join the leaderboard")
async def join_leaderboard(interaction: discord.Interaction, discord_id: str, steam_id: str):
    check = data_updater.update_data(discord_id, steam_id)
    if check is True:
        await interaction.response.send_message("User added to the leaderboard")
    else:
        await interaction.response.send_message("User is already on the leaderboard")

@bot.tree.command(name="leave_leaderboard", description="allows a user to join the leaderboard")
async def leave_leaderboard(interaction: discord.Interaction, discord_id: str):
    check = data_updater.remove_data(discord_id)
    if check is True:
        await interaction.response.send_message("User removed from the leaderboard")
    else:
        await interaction.response.send_message("User is not on the leaderboard")

@bot.event
async def on_ready():
    await bot.tree.sync()
    print("Command tree synced")

print("Local commands:", bot.tree.get_commands())
token = str(os.getenv("DISCORD_TOKEN"))
bot.run(token)
