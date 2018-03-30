from bs4 import BeautifulSoup
import requests

URL = "https://www.imdb.com/chart/boxoffice"
data = requests.get(URL).text

soup = BeautifulSoup(data, 'html.parser')

cols = soup.find_all('td', attrs={'class': 'titleColumn'})

with open('MovieID', 'w') as file:
    for col in cols:
        current_col = ('tt' + col.find('a').get('href').split('?')
                       [0].strip('/title/'))
        file.write(current_col + ',')
