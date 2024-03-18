from django.http import JsonResponse, HttpResponse
import pandas as pd
import requests
from django.shortcuts import render
from geopy.distance import geodesic
import json
import os
from .openData import CrowdManagement
from PMR_pythonAPI.settings import BASE_DIR


def arrets_de_bus_zone_Charleroi(request):
    # Call function from bus_stops_logic module to get bus stop data for Charleroi
    data = CrowdManagement.get_bus_stops_in_charleroi()
    return JsonResponse(data)


def documentation_Charleroi(request):
    return render(request, 'stop_charleroi.html')


def arret_de_bus_zone_Namur(request):
    # Call function from bus_stops_logic module to get bus stop data for Namur
    data = CrowdManagement.get_bus_stops_in_namur()
    return JsonResponse(data)

def documentation_namur(request):
    return render(request, 'stop_namur.html')


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
            return HttpResponse(json.dumps(response_data), content_type='application/json')
        else:
            # Si une des stations n'est pas trouvée, retourner une réponse avec un code d'erreur approprié
            return HttpResponse(status=404)
    else:
        # Si le fichier n'existe pas, retourner une réponse avec un code d'erreur approprié
        return HttpResponse(status=404)


def documentationInstallations(request):
    return render(request, 'facilities_docu.html')


def getFacilitiesOfATrain(request, id):
    url = 'https://api.irail.be/composition/?format=json&id=IC' + f'={id}'
    response = requests.get(url)

    if response.status_code == 200:
        json_data = response.json()
        return JsonResponse(json_data)
    else:
        return None


def documentationTrain(request):
    return render(request, 'jsonComp.html')


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


def documentationCrowdCharleroi(request):
    return render(request, 'crowdManagementCharleroi.html')


def documentationCrowdNamur(request):
    return render(request, 'crowdManagementNamur.html')


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


def GetScoreView(request):
    return render(request, 'ScoreDesc.html')
