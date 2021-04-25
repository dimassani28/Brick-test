# Python program to scrape website
# and save quotes from website
import requests
from bs4 import BeautifulSoup
import csv
from selenium import webdriver


URL = "https://www.tokopedia.com/p/handphone-tablet/handphone"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

quotes = []  # a list to store quotes

table = soup.find('div', attrs={'data-testid': 'lstCL2ProductList'})

for row in table.findAll('div',
                         attrs={'class': 'css-bk6tzz e1nlzfl3'}):
    quote = {}
    quote['name'] = row.find('div', class_='css-1bjwylw')
    quote['description'] = row.find('div', class_='css-vbihp9')
    quote['img'] = row.img['src']
    quote['price'] = row.find('div', class_='css-1beg0o7')
    quote['rating'] = len(row.find('div', class_='css-177n1u3'))
    quote['store'] = row.find('div', class_='css-1kr22w3')
    quotes.append(quote)

filename = 'tokopedia.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f, ['name', 'description', 'img', 'price', 'rating', 'store'])
    w.writeheader()
    for quote in quotes[0:100]:
        w.writerow(quote)