import os
from PMR_pythonAPI.settings import BASE_DIR
import pandas as pd

def get_stations_name():
    csv_file_path = os.path.join(BASE_DIR, 'pythonAPI_PMR/internData/stations.csv')
    stations = pd.read_csv(csv_file_path)

    # Filter the DataFrame where 'country-code' is 'be'
    stations = stations[stations['country-code'] == 'be']

    # Extract the 'name', 'longitude', and 'latitude' columns
    stations_info = stations[['name', 'longitude', 'latitude']]

    # Convert the DataFrame to a list of dictionaries
    stations_info_list = stations_info.to_dict('records')

    return stations_info_list

print(get_stations_name())