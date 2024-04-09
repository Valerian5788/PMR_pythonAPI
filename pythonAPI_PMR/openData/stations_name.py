import os
from PMR_pythonAPI.settings import BASE_DIR
import pandas as pd

def get_stations_name():
    csv_file_path = os.path.join(BASE_DIR, 'pythonAPI_PMR/internData/stations.csv')
    stations = pd.read_csv(csv_file_path)
    #only have the name column
    stations_name = stations['name']

    json_data = stations_name.to_json(orient='records')
    return json_data

print(get_stations_name())