# web scraper script which gets the data of endangered species from the web and stores them in a csv file.


# WARNING !!!!!!! 
# HOW TO INSTALL REQUESTS , BEAUTIFUL SOUP
# 1. pip install requests
# 2. pip install beautifulsoup4
# EXECUTE THE ABOVE TWO COMMANDS IN COMMAND PROMPT TO INSTALL THE LIBRARIES ESSENTIAL FOR THE EXECUTION OF THE SCRIPT

# IGNORE THE FOLLOWING COMMENT BLOCK !!!!
# Endangered = Endangered species.
# Threatened = Threatened species.
# Endangered (S/A) = Endangered based on similarity of appearance to an existing listed species.
# Threatened (S/A) = Threatened based on similarity of appearance to an existing listed species.
# XE = Essential experimental population.
# XN = Nonessential experimental population (See subpart H of this part).


import requests
from bs4 import BeautifulSoup
import csv

source = requests.get('https://awionline.org/content/list-endangered-species').text
soup = BeautifulSoup(source, 'lxml')

# print(soup.prettify()) # DEBUG PURPOSES --> html source code for website

article = soup.find('article')

# print(article.prettify()) # DEBUG PURPOSES --> html source for article containing list of endangered species

headings = []

for h1 in article.find_all('h1'):
	headings.append(h1.text)

headings.pop()

for h2 in article.find_all('h2'):
	headings.append(h2.text)

# print(headings)
# print()

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
