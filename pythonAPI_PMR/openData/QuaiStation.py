import requests

def get_hauteur_quai(station):
    url = f"https://opendata.infrabel.be/api/explore/v2.1/catalog/datasets/perronhoogten-in-stations/records?select=*&where=longnamefrench%20LIKE%20%27{station}%27&limit=99"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        stations = []
        for result in data["results"]:
            station_data = {
                "nom de la station": result["longnamefrench"],
                "quai": result["quai"],
                "Type de quai": result["platform_type"],
                "Hauteur": result["hauteur"],
                "Coordonnées": result["geo_point_2d"]
            }
            stations.append(station_data)
        return stations
    else:
        return None


