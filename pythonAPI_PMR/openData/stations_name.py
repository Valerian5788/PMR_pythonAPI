
import pandas as pd

def get_stations_name(lang):
    csv_file_path = f'pythonAPI_PMR/internData/belgian_stations_{lang}.csv'
    stations = pd.read_csv(csv_file_path)

    # Extract the 'name', 'longitude', and 'latitude' columns
    stations_info = stations[['Name','Latitude','Longitude']]

    # Convert the DataFrame to a list of dictionaries
    stations_info_list = stations_info.to_dict('records')

    return stations_info_list
