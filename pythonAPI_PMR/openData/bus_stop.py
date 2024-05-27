import requests

from pythonAPI_PMR.openData.station_coordinates import get_station_coordinates_french

def get_bus_stops_around_station(city_name, lat, lon, radius):
    # Convert lat and lon to float
    lat = float(lat)
    lon = float(lon)

    # Define the zone around the given coordinates
    min_lat = lat - radius
    max_lat = lat + radius
    min_lon = lon - radius
    max_lon = lon + radius

    # Construct the API URL with the search parameters
    url = (f"https://www.odwb.be/api/explore/v2.1/catalog/datasets/gtfs_tec_stops/records?"
           f"select=*&where=stop_name%20like%20%27{city_name.upper()}%27&order_by=stop_name&limit=99")

    # Make a request to the API
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
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
        # Return the JSON data of the stops in the zone
        return {"arret_autour_zone": arrets_dans_zone, "total des arrets dans la zone": len(arrets_dans_zone)}
    else:
        # Handle errors
        return {"error": f"Erreur lors de la récupération des données API, status code: {response.status_code}"}


