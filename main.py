import discord
from dotenv import load_dotenv
import os
from discord.ext import commands

import data_updater
import steam_hours

load_dotenv()

steam_api = str(os.getenv("STEAM_API_KEY"))

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
async def leave_leaderboard(interaction: discord.Interaction):
    discord_id = str(interaction.user.id)
    check = data_updater.remove_data(discord_id)
    if check is True:
        await interaction.response.send_message("User removed from the leaderbord")
    else:
        await interaction.response.send_message("User is not on the leaderboard")

@bot.tree.command(name="get_hours", description="gets total hours played on steam")
async def get_hours(interaction: discord.Interaction):
    discord_id = str(interaction.user.id)

    data = data_updater.get_data()
    if discord_id in data:
        steam_id = data[discord_id]

        hours = steam_hours.get_hours(steam_id, steam_api)
        await interaction.response.send_message(f"Your have played {hours:.2f} hours on steam")
    else:
        await interaction.response.send_message("Your information has not been added to the leaderboard, please use /join_leaderboard")

@bot.event
async def on_ready():
    await bot.tree.sync()
    print("Command tree synced and bot is ready")

token = str(os.getenv("DISCORD_TOKEN"))
bot.run(token)
