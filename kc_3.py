import json
import os
import requests
import time

# Define our two functions.
def is_website_green(website_dict: dict) -> str | bool:
    return website_dict['green']

def sort_by_cleanliness(website_dicts: list) -> list:
    return sorted(website_dicts, key=lambda dict: dict['cleanerThan'], reverse=True)

def is_cache_expired() -> bool:
    last_modified_seconds = os.path.getmtime('website_data.json')
    current_seconds = time.time()
    diff_seconds = current_seconds - last_modified_seconds

    return diff_seconds > 60*60*24

def get_data(websites) -> list:
    website_json = []

    if is_cache_expired():
        for website in websites:
            print(f'Retrieving data for {website}...')
            website_json.append(requests.get(f'https://api.websitecarbon.com/site?url={website}').json())

        with open("website_data.json", "w") as open_file:
            open_file.write(website_json)
            
        return website_json

    with open("website_data.json", 'r') as open_file:
        website_json = json.load(open_file)

    return website_json

# Import data.
websites = ['yahoo.com', 'ibm.com', 'roll20.net', 'facebook.com', 'netflix.com']
website_json = []

for website in websites:
    print(f'Retrieving data for {website}...')
    website_json.append(requests.get(f'https://api.websitecarbon.com/site?url={website}').json())

# Serialize our JSON as a string.
json_object = json.dumps(website_json, indent = 4)
  
# Write that string to our output file.
with open("website_data.json", "w") as open_file:
    open_file.write(json_object)

with open("website_data.json", 'r') as open_file:
    website_dicts = json.load(open_file)

# Call our functions.
green_websites_dicts = filter(lambda website: is_website_green(website) == True, website_dicts)

percentage_clean_websites = (len(green_websites_dicts) / len(website_dicts)) * 100
print(f'{percentage_clean_websites}% of tested websites were green.')

sorted_website_dicts = sort_by_cleanliness(website_dicts)
for website_dict in sorted_website_dicts:
    print(f'{website_dict["url"]}: {website_dict["cleanerThan"]}')

