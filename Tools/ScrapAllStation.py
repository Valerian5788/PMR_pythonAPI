import cloudscraper
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.belgiantrain.be/fr/station-information'

scraper = cloudscraper.create_scraper()

r = scraper.get(url)
print(r.status_code)

html_doc = r.text
soup = BeautifulSoup(html_doc)


df = pd.DataFrame([
    (
        item.get_text().strip(),
        item['href'],
    ) for item in soup.find_all('a')
    if item['href'].startswith('/fr/station-information/')
], columns=['name', 'url'])

print(df)

df.to_csv('stations_url.csv', index=False)