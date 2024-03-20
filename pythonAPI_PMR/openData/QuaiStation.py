import requests


def get_hauteur_quai(station):
    url = f"https://opendata.infrabel.be/api/explore/v2.1/catalog/datasets/perronhoogten-in-stations/records?select=*&where=longnamefrench%20LIKE%20%27{station}%27&limit=99"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()["results"]
        extracted_data = []
        for result in data:
            station_data = {
                "nom de la gare": result["longnamefrench"],
                "id du quai": result["quai"],
                "hauteur": result["hauteur"],
                "coordonnées": result["geo_point_2d"]
            }
            extracted_data.append(station_data)

        #extracted_data.sort(key=lambda x: int(x["id du quai"]))
        return  extracted_data
    else:
        return None

station = "NAMUR"
sorted_hauteurs_quais = get_hauteur_quai(station)
if sorted_hauteurs_quais:
    for station_data in sorted_hauteurs_quais:
        print(station_data)
else:
    print("Erreur lors de la récupération des données.")