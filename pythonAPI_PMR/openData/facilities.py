import json
import os
from PMR_pythonAPI.settings import BASE_DIR

def get_facilities_data():
    # Chemin vers le fichier facilities.json dans votre projet
    json_file_path = os.path.join(BASE_DIR, 'pythonAPI_PMR//internData/facilities.json')

    # Vérifier si le fichier existe
    if os.path.exists(json_file_path):
        # Ouvrir et lire le contenu du fichier JSON
        with open(json_file_path, 'r') as file:
            json_data = json.load(file)

        # Filtrer les données pour obtenir seulement la station "Charleroi-Central" et "Namur"
        charleroi_data = next((station for station in json_data if station["station"] == "Charleroi-Central"), None)
        namur_data = next((station for station in json_data if station["station"] == "Namur"), None)

        if charleroi_data and namur_data:
            # Créer un dictionnaire contenant les données des deux stations
            response_data = {
                "Charleroi-Central": charleroi_data["facilities"],
                "Namur": namur_data["facilities"]
            }
            return response_data
        else:
            return print("Les données pour les stations 'Charleroi-Central' et 'Namur' n'ont pas été trouvées.")
    else:
        return print("Le fichier facilities.json n'existe pas.")

print(get_facilities_data())