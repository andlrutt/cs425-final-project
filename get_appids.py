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
for x in range(0, len(apps)-3):
    random_appids.append(apps[rand_indices[x]]['appid'])

total_review_count = 0
dataset_app_ids = []
for app_id in random_appids:
    response = requests.get(f"https://store.steampowered.com/appreviews/{app_id}?json=1")
    review_count = response.json()['query_summary']['total_reviews']
    if (review_count > 100):
        total_review_count += review_count
        dataset_app_ids.append(app_id)
        print(f"{total_review_count} - {len(dataset_app_ids)}")
    if (total_review_count > 300000):
        break



[print(x) for x in dataset_app_ids]