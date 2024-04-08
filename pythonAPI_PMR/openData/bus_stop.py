import requests

from pythonAPI_PMR.openData.station_coordinates import get_station_coordinates_french


def get_bus_stops_around_station(city_name, station_name, radius):
    # renverser order by et changer limit ? voir avec order by pour tri ? ><
    # normalement on peut comparer deux string mais y'a erreur pour le moment
    # changer url avec les params (fonction à part)
    # Coordonnées géographiques de la gare de Namur
    coordonnees = get_station_coordinates_french(station_name)
    if 'lat' in coordonnees and 'lon' in coordonnees:
        lon = float(coordonnees['lon'])
        lat = float(coordonnees['lat'])
        # Continue with the rest of your code
    else:
        return {"error": "Latitude or longitude not found in station coordinates"}

    # Définition de la zone autour de la gare (namur pour le test)
    min_lat = lat - radius
    max_lat = lat + radius
    min_lon = lon - radius
    max_lon = lon + radius

    # Construction de l'URL de l'API avec les paramètres de recherche
    url = (f"https://www.odwb.be/api/explore/v2.1/catalog/datasets/gtfs_tec_stops/records?"
           f"select=*&where=stop_name%20like%20%27{city_name.upper()}%27&order_by=stop_name&limit=99")

    # Requête à l'API
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        total_count = data["total_count"]
        print(total_count)
        arrets_dans_zone = []
        for result in data["results"]:
            if "stop_id" in result and "stop_name" in result and "stop_coordinates" in result and min_lat < \
                    result["stop_coordinates"]["lat"] < max_lat and min_lon < result["stop_coordinates"][
                    "lon"] < max_lon:
                stop_info = {
                    "stop_id": result["stop_id"],
                    "stop_name": result["stop_name"],
                    "stop_coordinates": result["stop_coordinates"]
                }
                arrets_dans_zone.append(stop_info)
        # Retourner les données JSON des arrêts dans la zone
        return {"arret_autour_zone": arrets_dans_zone, "total des arrets dans la zone": len(arrets_dans_zone)}
    else:
        # Gestion des erreurs
        return {"error": f"Erreur lors de la récupération des données API, status code: {response.status_code}"}


print(get_bus_stops_around_station("Namur", "GaredeNamur", 0.005))
