import data_updater

data = data_updater.get_data()

new_data = {}

sunday_hours = [3000, 5, 15, 11000, 67, 100]

i = 0
for discord_id, id_and_hours in data.items():
    hours = id_and_hours["monday_hours"]
    new_hours = sunday_hours[i] - hours
    new_data[discord_id] = new_hours
    i = i + 1

sorted_data = sorted(new_data.items(), key=lambda item: item[1], reverse=True)

for discord_id, hours in sorted_data:
    print(f"Discord ID {discord_id} Hours: {hours}") 

winner_id, winner_hours = sorted_data[0]
print("##################################")
print("!!!!!!!!!!!!!!Winner!!!!!!!!!!!!!!")
print(f"Discord id: {winner_id} Hours played: {winner_hours}")
