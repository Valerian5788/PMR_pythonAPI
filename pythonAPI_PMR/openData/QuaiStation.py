import requests


def get_hauteur_quai(station):
    parsed_station = parse_station_name(station)

    url_french = f"https://opendata.infrabel.be/api/explore/v2.1/catalog/datasets/perronhoogten-in-stations/records?select=*&where=longnamefrench%20LIKE%20%27{parsed_station}%27&limit=99"
    url_dutch = f"https://opendata.infrabel.be/api/explore/v2.1/catalog/datasets/perronhoogten-in-stations/records?select=*&where=longnamedutch%20LIKE%20%27{parsed_station}%27&limit=99"
    response = requests.get(url_french)
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

        extracted_data.sort(key=lambda x: int(x["id du quai"]))
        return {"donnees quai : ": extracted_data}

    elif response.status_code == 404:
        response = requests.get(url_dutch)
        if response.status_code == 200:
            data = response.json()["results"]
            extracted_data = []
            for result in data:
                station_data = {
                    "nom de la gare": result["longnamedutch"],
                    "id du quai": result["quai"],
                    "hauteur": result["hoogte"],
                    "coordonnées": result["geo_point_2d"]
                }
                extracted_data.append(station_data)

            extracted_data.sort(key=lambda x: int(x["id du quai"]))
            return {"donnees quai : ": extracted_data}
        else:
            return None



def parse_station_name(station_name):
    return station_name.split("/")[0]
