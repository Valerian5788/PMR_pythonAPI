import requests


def get_station_coordinates_french(station_name):
    station_name = station_name.replace(" ", "+")
    # Construction de l'URL de l'API avec les paramètres de recherche
    url = f"https://geocode.maps.co/search?q={station_name}&api_key=660e97aa661dc573620980olb7f84dd"

    # Requête à l'API
    response = requests.get(url)
    coordonnees = {}
    if response.status_code == 200:
        data = response.json()
        for result in data:
            if result["type"] == "train_station":
                coordonnees = {
                    "lat": result["lat"],
                    "lon": result["lon"]
                }
        # Retourner les données JSON des coordonnées de la gare
        return coordonnees
    else:
        # Gestion des erreurs
        return {"error": f"Erreur lors de la récupération des données API, status code: {response.status_code}"}


