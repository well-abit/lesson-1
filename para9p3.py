import requests
from bs4 import BeautifulSoup

response = requests.get("https://coinmarketcap.com/")

if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("div", attrs={"class": "sc-631098c-0 iJZToW"})

    if len(soup_list) > 1:
        res = soup_list[1].find("span")
        if res:
            print(res.text)