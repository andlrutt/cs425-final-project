import requests
import random
random.seed(42)

response = requests.get('https://api.steampowered.com/ISteamApps/GetAppList/v2/')

apps = response.json()['applist']['apps']

# filter blank/non-english names
apps = [x for x in apps if x['name'] != '' and x['name'].isascii()]

random_apps = []
for x in range(0, 10000):
    random_apps.append(apps[random.randint(0,len(apps)-1)])

[print(x['appid']) for x in random_apps]