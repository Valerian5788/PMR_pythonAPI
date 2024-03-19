from django.http import JsonResponse, HttpResponse
import requests
from django.shortcuts import render
from .openData import CrowdManagement, facilities, bus_stop, TrainInfos



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
        json_data = TrainInfos.getFacilitiesOfATrain(id)
        return JsonResponse(json_data)
    else:
        return HttpResponse(status=404)

def getCrowdManagementOfDayCharleroi(request, day):
    # Convert filtered data to JSON
    json_data = CrowdManagement.getCrowdManagementOfDayCharleroi(day)

    # Return JSON response
    return JsonResponse(json_data, safe=False)


def getCrowdManagementOfDayNamur(request, day):
    # Convert filtered data to JSON
    json_data = CrowdManagement.getCrowdManagementOfDayNamur(day)

    # Return JSON response
    return JsonResponse(json_data, safe=False)


#documentations

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
