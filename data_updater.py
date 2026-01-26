import json

def get_data():
    with open("data.json", "r") as f:
        data = json.load(f)

    return data

def update_data(discord_id, steam_id):

    with open("data.json", "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = {}
    
    if discord_id not in data:
        data[str(discord_id)] = str(steam_id)
    else:
        return False

    with open("data.json", "w") as f:
        json.dump(data, f, indent=2)

    return True

def remove_data(discord_id):

    with open("data.json", "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = {}

    if discord_id in data:
        del data[discord_id]
    else:
        return False

    with open("data.json", "w") as f:
        json.dump(data, f, indent=2)

    return True
