import json

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