import requests
from bs4 import BeautifulSoup
import csv

s = open('anime_list.csv', 'w', newline='')
s.write('Index;Name;Year;IMDB\n')

#top_100 = csv.writer(s)
#top_100.writerow(['Index', 'Name', 'Year', 'IMDB'])

h = {'Accept-Language': 'en-US'}
url = 'https://www.imdb.com/list/ls057577566/?sort=moviemeter,asc&st_dt=&mode=detail&page=1&ref_=ttls_vm_dtl'
r = requests.get(url, headers=h)


soup = BeautifulSoup(r.text, 'html.parser')
list = soup.find('div', {'class': 'lister-list'})

all_animes = list.find_all('div', {'class': 'lister-item'})

for anime in all_animes:
    index = anime.span.text
    index = index.replace('.', '')
    name = anime.h3.a.text
    year = anime.find('span', {'class': 'lister-item-year'}).text
    year = year.replace('(', '')
    year = year.replace(')', '')
    imdb = anime.find('span', {'class': 'ipl-rating-star__rating'}).text
    imdb = imdb.replace('.', ',')
#    top_100.writerow([index, name, year, imdb])

    s.write(index+';'+name+';'+year+';'+imdb+'\n')




