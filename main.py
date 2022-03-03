import requests
from bs4 import BeautifulSoup

date = input('Which year do you want to travel to? Type the date in the format YYYY-MM-DD:')

URL = f'https://www.billboard.com/charts/hot-100/{date}'

response = requests.get(URL)
website = response.text

soup = BeautifulSoup(website, 'html.parser')

get_songs = soup.select(selector='li ul li h3')

songs = [title.getText().strip('\n') for title in get_songs]

print(songs)