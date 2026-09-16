# Steam Leader-board bot

Discord bot made using discord.py, it makes a leader-board based of the weekly hours on steam and the person with the most hours in a week wins.

---
## Table of Contents

- [About](#about)
- [Features](#features)
- [Configuration](#configuration)
- [Installation](#installation)
- [License](#License)

## About
This is a for fun project mainly to practice python and self hosting my own bot on a home lab

---
## Features

Ping - Simple check to see if bot is alive
```
/ping
```

---
Join Leader-board - Requires an input if steam_id which you can get off your profile link
should look like this
https://steamcommunity.com/profiles/12345....17_digit_number/
```
/join_leaderboard steam_id:
```

---

Leave Leader-board - Checks if you are in the leader-board and then either kicks you or prompts you to sign up
```
/leave_leaderboard
```

---
Get Hours - If in the leader-board you can get the total amount of hours played on steam
```
/get_hours
```

---
List Players And Wins - Lists all the players and the amount of wins they have
```
/list_players_and_wins
```

---
Set Leader-Board chat : Sets the channel that the bot will post in, just go the the aspired channel and input the command
```
/set_leaderboard
```

---
## Configuration
You need to input 2 values into the `.env.template` file your steam api key and the bot token
You can get both off
[[STEAM_API_KEY]](https://steamcommunity.com/dev)
[BOT_TOKEN](https://discord.com/developers/applications)

| Variable        | Description                              |
| --------------- | ---------------------------------------- |
| `STEAM_API_KEY` | Steam API Key                            |
| `BOT_TOKEN`     | Bot token so the code knows where to run |
After both are filled in please rename `.env.template` to `.env`

---
## Installation

```bash
# Clone the repo
git clone https://github.com/xkuba7/discord_bot.git
cd discord_bot

# Install and run the bot
sudo docker compose up -d
```

---
## License
This project is licensed under the GNU General Public License v3.0 see the [LICENSE](LICENSE) file for details