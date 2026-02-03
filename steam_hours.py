import requests

def get_hours(steam_id, steam_api):
    steam_id = str(steam_id)
    steam_api = str(steam_api)

    steam_url = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/"
    params = {
        "key": steam_api,
        "steamid": steam_id,
        "format": "json",
        "include_played_free_games": "true"
        }

    response = requests.get(steam_url, params=params)
    data = response.json()

    game_count = data["response"]["game_count"]
    total = 0
    for i in range(game_count):
        game_time = data["response"]["games"][i]["playtime_forever"]
        total += round(game_time / 60, 1)

    return total
