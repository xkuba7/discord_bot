import json

def get_data():

    with open("data.json", "r") as f:
        data = json.load(f)

    return data

def save_data(data):
    with open("data.json", "w") as f:
        json.dump(data, f, indent=2)

def add_player(discord_id, steam_id):

    data = get_data()
    #with open("data.json", "r") as f:
    #    try:
    #        data = json.load(f)
    #    except json.JSONDecodeError:
    #        data = {}
    
    if discord_id not in data:
        data[str(discord_id)] = {"steam_id": str(steam_id), "monday_hours": 0}
    else:
        return False

    save_data(data)
    return True

def remove_player(discord_id):

    data = get_data()
    #with open("data.json", "r") as f:
    #    try:
    #        data = json.load(f)
    #    except json.JSONDecodeError:
    #        data = {}

    if discord_id in data:
        del data[discord_id]
    else:
        return False

    save_data(data)
    return True

def add_monday_hours(discord_id, hours):

    data = get_data()
    data[str(discord_id)]["monday_hours"] = hours 

    save_data(data)
