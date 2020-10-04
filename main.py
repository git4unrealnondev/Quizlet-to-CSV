import requests
import lxml
from bs4 import BeautifulSoup

import sys
import csv

def main(UserInput):
	UserInput.pop(0)
	print (UserInput)
	header = {'User-Agent': 'My User Agent 1.0'}
	isfirst = True
	with open('quizlet.csv', 'w', newline='') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		for x in UserInput:
			
			source = requests.get(x, headers=header).text
			soup = BeautifulSoup(source, 'lxml')
			first = soup.find_all("span", class_="TermText notranslate lang-en")
			
			##parsed = first.TermText notranslate lang-en
			#print (soup.prettify())
			
				
			for x in first:
				if isfirst:
					doublearray = [x.text]
					isfirst = False
				else:
					doublearray.append(x.text)
					spamwriter.writerow(doublearray)
					doublearray = []
					isfirst = True
	csvfile.close()
## Checks if user has entered a URL.
if (len(sys.argv) > 1):
	main(sys.argv)
