from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .openData import CrowdManagement, facilities, bus_stop, TrainInfos, QuaiStation, stations_name


def arrets_de_bus_zone(request):
    # Call function from bus_stops_logic module to get bus stop data for Namur
    city_name = request.GET.get('c')
    station_name = request.GET.get('s')
    radius = float(request.GET.get('r'))  # Convert to float or int as needed
    data = bus_stop.get_bus_stops_around_station(city_name, station_name, radius)
    return JsonResponse(data)


def get_all_facilities(request):
    facilities_data = facilities.get_facilities_data()
    if facilities_data:
        return JsonResponse(facilities_data)
    else:
        return HttpResponse(status=404)


def getFacilitiesOfATrain(request, id):
    json_data = TrainInfos.getFacilitiesOfATrain(id)
    if json_data:
        return JsonResponse(json_data, safe=False)
    else:
        return HttpResponse(status=404)

def getStationsName(request):
    json_data = stations_name.get_stations_name()
    if json_data:
        return JsonResponse(json_data, safe=False)
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


def GetHauteurQuaiByCity(request, city):
    json_data = QuaiStation.get_hauteur_quai(city)

    if json_data:
        return JsonResponse(json_data)
    else:
        return HttpResponse(status=400)


# documentations

# /apiScoreDoc
def GetDocumentationView(request):
    return render(request, 'ScoreDesc.html')


# /NamurTri/<str:day>
def documentationCrowdNamur(request):
    return render(request, 'crowdManagementNamur.html')


# /CharleroiTri/<str:day>
def documentationCrowdCharleroi(request):
    return render(request, 'crowdManagementCharleroi.html')


# /compositionDocumentation
def documentationTrain(request):
    return render(request, 'jsonComp.html')


# /jsonComposition/<int:id>
def documentationInstallations(request):
    return render(request, 'facilities_docu.html')


# /bus/
def documentation_bus(request):
    return render(request, 'stop_bus.html')
