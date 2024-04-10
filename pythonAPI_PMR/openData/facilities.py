import json
import os
from PMR_pythonAPI.settings import BASE_DIR

def get_facilities_data():
    json_file_path = os.path.join(BASE_DIR, 'pythonAPI_PMR//internData/facilities.json')

    if os.path.exists(json_file_path):
        with open(json_file_path, 'r') as file:
            json_data = json.load(file)

        # Remove null parameters and sort the JSON data
        for station in json_data:
            station = {k: v for k, v in station.items() if v is not None}

        sorted_json_data = json.dumps(json_data, sort_keys=True)

        return sorted_json_data
    else:
        return "Le fichier facilities.json n'existe pas."

print(get_facilities_data())