from django.http import JsonResponse, HttpResponse
import pandas as pd
import requests
from django.shortcuts import render
from .openData import CrowdManagement, facilities, bus_stop



def arrets_de_bus_zone_Charleroi(request):
    # Call function from bus_stops_logic module to get bus stop data for Charleroi
    data = bus_stop.get_bus_stops_in_charleroi()
    return JsonResponse(data)
#erreur: CrowdManagement pas au bon endroit


def arrets_de_bus_zone_Namur(request):
    # Call function from bus_stops_logic module to get bus stop data for Namur
    data = bus_stop.get_bus_stops_in_namur()
    return JsonResponse(data)

def get_all_facilities(request):
    facilities_data = facilities.get_facilities_data()
    if facilities_data:
        return JsonResponse(facilities_data)
    else:
        return HttpResponse(status=404)

def getFacilitiesOfATrain(request, id):
    url = 'https://api.irail.be/composition/?format=json&id=IC' + f'={id}'
    response = requests.get(url)

    if response.status_code == 200:
        json_data = response.json()
        return JsonResponse(json_data)
    else:
        return None

def getCrowdManagementOfDayCharleroi(request, day):
    # Convert filtered data to JSON
    json_data = CrowdManagement.getCrowdManagementOfDayCharleroi(day)

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


#documentaions

#/apiScoreDoc
def GetScoreView(request):
    return render(request, 'ScoreDesc.html')

#/NamurTri/<str:day>
def documentationCrowdNamur(request):
    return render(request, 'crowdManagementNamur.html')

#/CharleroiTri/<str:day>
def documentationCrowdCharleroi(request):
    return render(request, 'crowdManagementCharleroi.html')

#/compositionDocumentation
def documentationTrain(request):
    return render(request, 'jsonComp.html')

#/jsonComposition/<int:id>
def documentationInstallations(request):
    return render(request, 'facilities_docu.html')

#/tecNamurCentral/
def documentation_bus_namur(request):
    return render(request, 'stop_namur.html')

#/tecCharleroiCentral/
def documentation_bus_Charleroi(request):
    return render(request, 'stop_charleroi.html')
