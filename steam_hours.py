import requests
from dotenv import load_dotenv

load_dotenv()

def get_hours(steam_id, steam_api):
    steam_id = str(steam_id)
    steam_api = str(steam_api)
    steam_url = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=" + steam_api + "&steamid=" + steam_id + "&format=json"

    response = requests.get(steam_url)
    data = response.json()

    game_count = data["response"]["game_count"]
    total = 0
    for i in range(game_count):
        game_time = data["response"]["games"][i]["playtime_forever"]
        # print(data["response"]["games"][i]["playtime_forever"])
        total += round(game_time / 60, 1)
        # print(round(game_time / 60, 1))

    return total
