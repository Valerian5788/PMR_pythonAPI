import json
import cloudscraper
from bs4 import BeautifulSoup
import pandas as pd

df_stations = pd.read_csv('stations_url.csv')
df_stations['url'] = 'https://www.belgiantrain.be' + df_stations['url']
print(df_stations)

scraper = cloudscraper.create_scraper()
def get_facilities(scraper, station_url):
    url = station_url
    r = scraper.get(url)
    if r.status_code == 200:
        html_doc = r.text
        soup = BeautifulSoup(html_doc)
        return [
            {
                'name': item['data-facility-name'],
                'value': item.get_text().strip().split('\r\n')[0],
            }
            for item in soup.find_all(
                'div',
                attrs={
                    'data-facility-name': True,
                }
            )
        ]
    else:
        print(f'Error with {url}: {r.status_code}, skipping')

stations = []
for i, station in enumerate(df_stations.to_dict(orient='records')):
    facilities = get_facilities(scraper, station['url'])
    stations.append({
        'station': station['name'],
        'facilities': facilities,
    })
with open('pythonAPI_PMR/facilities.json', 'w') as f:
    json.dump(stations, f)