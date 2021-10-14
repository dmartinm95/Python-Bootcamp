import requests
from bs4 import BeautifulSoup

date = input(
    "Which year do you want to travel to? Type the date in this format: YYYY-MM-DD: ")

base_url = "https://www.billboard.com/charts/hot-100/"

resonse = requests.get(base_url + date)

soup = BeautifulSoup(resonse.text, "html.parser")

songs = [song.getText() for song in soup.find_all(
    name="span", class_="chart-element__information__song text--truncate color--primary")]


print("Top 100 songs from " + date)

i = 1
for song in songs:
    print('%d) %s' % (i, song))
    i += 1
