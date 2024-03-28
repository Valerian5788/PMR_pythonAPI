import requests

def get_bus_stops_in_charleroi():
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
            if "stop_id" in result and "stop_name" in result and "stop_coordinates" in result:
                stop_info = {
                    "stop_id": result["stop_id"],
                    "stop_name": result["stop_name"],
                    "stop_coordinates": result["stop_coordinates"]
                }
                arrets_dans_zone.append(stop_info)

        # Retourner les données JSON des arrêts dans la zone
        return {"arret_autour_zone": arrets_dans_zone}
    else:
        # Gestion des erreurs
        return {"error": "Erreur lors de la récupération des données API"}

def get_bus_stops_in_namur():
    # Coordonnées géographiques de la gare de Namur
    lat = 50.466667  # Latitude en décimal
    lon = 4.866667  # Longitude en décimal
    radius = 0.02  # Rayon de la zone autour de la gare (5 km = 0.05 degré en approximation)

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
            if "stop_id" in result and "stop_name" in result and "stop_coordinates" in result:
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
        return {"error": "Erreur lors de la récupération des données API"}
