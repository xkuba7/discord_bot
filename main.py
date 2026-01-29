import datetime
import discord
from dotenv import load_dotenv
import os
from discord.ext import commands, tasks

import data_updater
import steam_hours

load_dotenv()

steam_api = str(os.getenv("STEAM_API_KEY"))

intents = discord.Intents.default()
intents.message_content = True

all_players_embed = discord.Embed(
    title="Leaderboard members",
    description="All the players",
    color=discord.Color.orange()
)

leaderboard_embed = discord.Embed(
    title="Leaderboard",
    description="Results of weekly hours",
    color=discord.Color.orange()
)

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
async def join_leaderboard(interaction: discord.Interaction, steam_id: str):
    discord_id = str(interaction.user.id)
    check = data_updater.add_player(discord_id, steam_id)
    if check is True:
        await interaction.response.send_message("User added to the leaderboard")
    else:
        await interaction.response.send_message("User is already on the leaderboard")

@bot.tree.command(name="leave_leaderboard", description="allows a user to join the leaderboard")
async def leave_leaderboard(interaction: discord.Interaction):
    discord_id = str(interaction.user.id)
    check = data_updater.remove_player(discord_id)
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

@bot.tree.command(name="list_players", description="lists all the players who joined the leaderboard")
async def list_players(interaction: discord.Interaction):
    data = data_updater.get_data()
    users = data.keys()

    for user in users:
        user = await bot.fetch_user(user)
        username = user.name
        all_players_embed.add_field(name=username, value="")

    all_players_embed.set_footer(text="Combustion Bot")
    await interaction.response.send_message(embed=all_players_embed)

@tasks.loop(time=datetime.time(hour=0, minute=0))
async def get_hours_monday():
    if datetime.datetime.now().weekday() == 0: # 0 is monday
        data = data_updater.get_data()
        
        # json file data looks like {discord_id: {steam_id: 123, monday_hours: 123}}
        for discord_id, id_and_hours in data.items():
            hours = steam_hours.get_hours(id_and_hours["steam_id"], steam_api)
            data_updater.add_monday_hours(discord_id, hours)

        print("Monday hours added")

channel_id = os.getenv("CHANNEL_ID")
@tasks.loop(time=datetime.time(hour=7, minute=28))
async def create_leaderboard():
    if datetime.datetime.now().weekday() == 3: # 6 is sunday
        data = data_updater.get_data()
        new_data = {}

        # get data and create new dictionary
        # json file data looks like {discord_id: {steam_id: 123, monday_hours: 123}}
        for discord_id, id_and_hours in data.items():
            monday_hours = id_and_hours["monday_hours"]
            sunday_hours = steam_hours.get_hours(id_and_hours["steam_id"], steam_api)
            new_hours = sunday_hours - monday_hours
            new_data[discord_id] = new_hours

        sorted_data = sorted(new_data.items(), key=lambda item: item[1], reverse=True)
        winner_id, winner_hours = sorted_data[0]

        # create embed to send
        i = 0
        for discord_id, hours in new_data.items():
            i = i + 1
            user = await bot.fetch_user(discord_id)
            username = user.name
            leaderboard_embed.add_field(name=f"{i}. {username}", value=f"{hours} hours")

        channel = bot.get_channel(int(channel_id))
        await channel.send(embed=leaderboard_embed)
        await channel.send(f"Winner is {f"<@{winner_id}>"} with {winner_hours} hours")

@bot.event
async def on_ready():
    await bot.tree.sync()
    print("Command tree synced and bot is ready")
    for cmd in bot.tree.get_commands():
        print(cmd.name)

    if not get_hours_monday.is_running():
        get_hours_monday.start()

    if not create_leaderboard.is_running():
        create_leaderboard.start()

token = str(os.getenv("DISCORD_TOKEN"))
bot.run(token)
