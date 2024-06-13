import requests
import pandas as pd

# URL de l'API SNCB pour obtenir les informations sur les gares
api_url = 'https://api.irail.be/stations/?format=json&lang=en'

# Effectuer la requête GET à l'API
response = requests.get(api_url)

# Vérifier si la requête a réussi
if response.status_code == 200:
    stations_data = response.json()['station']
    
    # Extraire les noms et coordonnées des gares
    stations_list = []
    for station in stations_data:
        name = station['name']
        latitude = station['locationY']
        longitude = station['locationX']
        stations_list.append([name, latitude, longitude])
    
    # Convertir en DataFrame pour une manipulation plus facile
    stations_df = pd.DataFrame(stations_list, columns=['Name', 'Latitude', 'Longitude'])
    
    # Sauvegarder le DataFrame dans un fichier CSV
    stations_df.to_csv('pythonAPI_PMR/internData/belgian_stations_en.csv', index=False)
    print("Les données des gares ont été sauvegardées dans 'belgian_stations.csv'")
else:
    print("Erreur lors de la requête à l'API:", response.status_code)
