# web scraper script which gets the data of endangered species from the web and stores them in a csv file.

import requests
from bs4 import BeautifulSoup
import csv

source = requests.get('https://awionline.org/content/list-endangered-species').text
soup = BeautifulSoup(source, 'lxml')


article = soup.find('article')


headings = []

for h1 in article.find_all('h1'):
	headings.append(h1.text)

headings.pop()

for h2 in article.find_all('h2'):
	headings.append(h2.text)


index = 0
# MAKING DATABASE OF ALL THE ENDANGERED SPECIES WHICH IS A CSV FILE
with open('database.csv','w', newline='') as db:
	csv_writer = csv.writer(db)

	for table in article.find_all('table'):
		csv_writer.writerow([])
		csv_writer.writerow([headings[index].upper(), ' ' , ' '])
		index = index + 1
		csv_writer.writerow(['COMMON NAME', 'SCIENTIFIC NAME' , 'STATUS'])
		

		rows = table.find_all('tr')
		for tr in rows:
			td = tr.find_all('td')
			row = [i.text for i in td]
			csv_writer.writerow(row)

db.close()
