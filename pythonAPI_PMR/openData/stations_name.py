import os
from PMR_pythonAPI.settings import BASE_DIR
import pandas as pd

def get_stations_name():
    csv_file_path = os.path.join(BASE_DIR, 'pythonAPI_PMR/internData/stations.csv')
    stations = pd.read_csv(csv_file_path)
    #only have the name column
    stations_name = stations['name'].tolist()
    return stations_name

print(get_stations_name())