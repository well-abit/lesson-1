import requests
from bs4 import BeautifulSoup

index = int(input("Введи номер валюти: "))

response = requests.get("https://coinmarketcap.com/")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list1 = soup.find_all("div", attrs={"class": "sc-4c05d6ef-0 fmdKtv"})
    soup_list = soup.find_all("div", attrs={"class": "sc-631098c-0 ilZTOW"})
    res1 = soup_list1[index].get_text()
    res = soup_list[index].find("span")

    print(f"Валюта:{res1} Вартість:{res}")
