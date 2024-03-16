from xmlrpc.client import DateTime

from django.http import JsonResponse, HttpResponse
import pandas as pd
import requests
from geopy.distance import geodesic

import requests
import requests
from django.http import JsonResponse
import json
import requests
from django.http import JsonResponse

from PMR_pythonAPI.settings import BASE_DIR


def arrets_de_bus_zone_Charleroi(request):
    import requests
    from django.http import JsonResponse

    # Coordonnées géographiques de la gare de Charleroi
    lat = 50.404444  # Latitude en décimal
    lon = 4.438611   # Longitude en décimal
    radius = 0.02  # Rayon de la zone autour de la gare (5 km = 0.05 degré en approximation)


    # Définition de la zone autour de la gare
    min_lat = lat - radius
    max_lat = lat + radius
    min_lon = lon - radius
    max_lon = lon + radius

    # Construction de l'URL de l'API avec les paramètres de recherche
    url = "https://www.odwb.be/api/explore/v2.1/catalog/datasets/gtfs_tec_stops/records?select=*&where=stop_name%20like%20%27Charleroi%27&limit=50"

    # Requête à l'API
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        arrets_dans_zone = []
        for result in data["results"]:
            if "stop_coordinates" in result:
                stop_coordinates = result["stop_coordinates"]
                if "lat" in stop_coordinates and "lon" in stop_coordinates:
                    stop_lat = float(stop_coordinates["lat"])
                    stop_lon = float(stop_coordinates["lon"])
                    if min_lat <= stop_lat <= max_lat and min_lon <= stop_lon <= max_lon:
                        arrets_dans_zone.append(result)
        # Retourner les données JSON des arrêts dans la zone
        print(len(arrets_dans_zone))
        print(arrets_dans_zone[1])
        return JsonResponse({"arret autour CharleroiCentral :":arrets_dans_zone})
    else:
        # Gestion des erreurs
        return JsonResponse({"error": "Erreur lors de la récupération des données API"}, status=500)


def arrets_de_bus_zone_Namur(request):


    # Coordonnées géographiques de la gare de Bruxelles
    lat = 50.466667  # Latitude en décimal
    lon = 4.866667   # Longitude en décimal
    radius = 0.01   # Rayon de la zone autour de la gare (5 km = 0.05 degré en approximation)

    # Définition de la zone autour de la gare
    min_lat = lat - radius
    max_lat = lat + radius
    min_lon = lon - radius
    max_lon = lon + radius

    # Construction de l'URL de l'API avec les paramètres de recherche
    url = "https://www.odwb.be/api/explore/v2.1/catalog/datasets/gtfs_tec_stops/records?select=*&where=stop_name%20like%20%27NAMUR%27&limit=99"

    # Requête à l'API
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        arrets_dans_zone = []
        for result in data["results"]:
            if "stop_coordinates" in result:
                stop_coordinates = result["stop_coordinates"]
                if "lat" in stop_coordinates and "lon" in stop_coordinates:
                    stop_lat = float(stop_coordinates["lat"])
                    stop_lon = float(stop_coordinates["lon"])
                    if min_lat <= stop_lat <= max_lat and min_lon <= stop_lon <= max_lon:
                        arrets_dans_zone.append(result)
        # Retourner les données JSON des arrêts dans la zone
        print(len(arrets_dans_zone))
        print(arrets_dans_zone[1])
        return JsonResponse({"arret autour de la gare de Namur :":arrets_dans_zone})
    else:
        # Gestion des erreurs
        return JsonResponse({"error": "Erreur lors de la récupération des données API"}, status=500)

from django.http import FileResponse
import os

def get_all_facilities(request):
    # Chemin vers le fichier facilities.json dans votre projet
    json_file_path = os.path.join(BASE_DIR, 'pythonAPI_PMR/facilities.json')

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
            # Retourner une réponse avec les installations des deux stations
            print(response_data)
            return HttpResponse(json.dumps(response_data), content_type='application/json')
        else:
            # Si une des stations n'est pas trouvée, retourner une réponse avec un code d'erreur approprié
            return HttpResponse(status=404)
    else:
        # Si le fichier n'existe pas, retourner une réponse avec un code d'erreur approprié
        return HttpResponse(status=404)
import requests

def getFacilitiesOfATrain(request, id):
    url = 'https://api.irail.be/composition/?format=json&id=IC' + f'={id}'
    response = requests.get(url)

    if response.status_code == 200:
        json_data = response.json()
        print(json_data)
        return JsonResponse(json_data)
    else:
        return None


def getCrowdManagementOfDayCharleroi(request, day):
    # Example of validating the format of the day string
    if len(day) != 6:
        return JsonResponse({'error': 'Invalid day format. Please provide day in ddmmyy format.'})

    # Read the CSV file
    charleroi = pd.read_csv("pythonAPI_PMR/donnéesCharleroi.csv")

    # Convert the 'timestamp' column to datetime with correct format
    charleroi['timestamp'] = pd.to_datetime(charleroi['timestamp'], format='%d/%m/%Y %H:%M:%S')

    # Convert day to the expected format (if needed)
    day_str_formatted = day[:2] + '/' + day[2:4] + '/' + day[4:]

    # Filter data for the specified day
    charleroi_filtered = charleroi[charleroi['timestamp'].dt.strftime('%d/%m/%y') == day_str_formatted]

    # Convert filtered data to JSON
    json_data = charleroi_filtered.to_dict(orient='records')

    # Return JSON response
    return JsonResponse(json_data, safe=False)
def getCrowdManagementOfDayNamur(request, day):
    # Example of validating the format of the day string
    if len(day) != 6:
        return JsonResponse({'error': 'Invalid day format. Please provide day in ddmmyy format.'})

    # Read the CSV file
    Namur = pd.read_csv("pythonAPI_PMR/donnéesNamur.csv")

    # Convert the 'timestamp' column to datetime with correct format
    Namur['timestamp'] = pd.to_datetime(Namur['timestamp'], format='%d/%m/%Y %H:%M:%S')

    # Convert day to the expected format (if needed)
    day_str_formatted = day[:2] + '/' + day[2:4] + '/' + day[4:]

    # Filter data for the specified day
    Namur_filtered = Namur[Namur['timestamp'].dt.strftime('%d/%m/%y') == day_str_formatted]

    # Convert filtered data to JSON
    json_data = Namur_filtered.to_dict(orient='records')

    # Return JSON response
    return JsonResponse(json_data, safe=False)

