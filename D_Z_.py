
#  ЗАДАНИЕ 1

#import re
#class Finder:
#    def __init__(self, pattern, text):
#        self.pattern = pattern
#        self.text = text
#    def __iter__(self):
#       for match in re.finditer(self.pattern, self.text):
#           yield match.group()



# ЗАДАНИЕ 2

import requests
from bs4 import BeautifulSoup
import lxml

url = 'https://kups.club/'

user = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 OPR/94.0.0.0'}


response = requests.get(url, headers=user)
print(response.status_code)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'lxml')
    #print(soup)
    all_product = soup.find('div', class_='row mt-4')
    #print(all_product)
    product = all_product.find_all('div', class_='col-lg-4 col-md-4 col-sm-6 portfolio-item')
    for prod in product:
        print(prod.text)
