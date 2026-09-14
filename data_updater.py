import json

DATA_FILE = "data.json"

def get_data():
    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    return data

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def add_player(discord_id, steam_id):

    data = get_data()

    if discord_id in data:
        return False

    data[str(discord_id)] = {"steam_id": str(steam_id), "monday_hours": 0, "total_wins": 0}

    save_data(data)
    return True

def remove_player(discord_id):

    data = get_data()

    if discord_id not in data:
        return False

    del data[discord_id]
    save_data(data)
    return True

def add_monday_hours(discord_id, hours):

    data = get_data()
    data[str(discord_id)]["monday_hours"] = hours 

    save_data(data)

def update_wins(discord_id):

    data = get_data()
    data[str(discord_id)]["total_wins"] += 1

    save_data(data)
