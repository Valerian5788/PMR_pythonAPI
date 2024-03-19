import requests


def get_hauteur_quai(station):
    url = f"https://opendata.infrabel.be/api/explore/v2.1/catalog/datasets/perronhoogten-in-stations/records?select=*&where=longnamefrench%20LIKE%20%27{station}%27&limit=99"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for result in data["results"]:
            json_data = {
                "nom de la station: ", data["longnamefrench"],
                "quai", data["quai"],
                "Type de quai", data["platform_type"],
                "Hauteur", data["hauteur"],
                "Coordonnées", data["geometry"]
            }
        return json_data
    else:
        return None