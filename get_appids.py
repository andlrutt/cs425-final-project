import requests
import random
import numpy as np
random.seed(42)

response = requests.get('https://api.steampowered.com/ISteamApps/GetAppList/v2/')

apps = response.json()['applist']['apps']

# filter blank/non-english names
apps = [x for x in apps if x['name'] != '' and x['name'].isascii()]

rand_indices = random.sample(range(len(apps)-1), len(apps)-2)
print(len(apps))

random_appids = []
for x in range(0, 1505):
    random_appids.append(apps[rand_indices[x]]['appid'])