import requests
from bs4 import BeautifulSoup
import lxml



url = "https://allo.ua/ua/televizory/smart_sistem_tv-da/"
user = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}


response = requests.get(url, headers=user)
print(response.status_code)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "lxml")
    # print(soup)

    all_product = soup.find("div", class_="products-layout__container products-layout--grid")
    # print(all_product)
    product = all_product.find_all("div", class_="product-card")
    for prod in product:
        print(prod.text)
    for prod in product:
        name = prod.find("a", class_="product-card__title")
        if name.text != "":
            print(name.text)
    for prod in product:
        old_price1 = prod.find("div", class_="v-pb")
        if old_price1.text != "":
            print(old_price1.text)