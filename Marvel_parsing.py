import requests as req
from bs4 import BeautifulSoup
import csv

MARVER_URL = "https://marvel.com"

response = req.get(
    "https://www.marvel.com/v1/pagination/grid_cards?offset=0&limit=1&sortDirection=ASC&sortField=title&entityType=character")

if response.status_code == 200:
    data = response.json()
    total = data["data"]["results"]["pagedata"]["total"]

    response = req.get(
        f"https://www.marvel.com/v1/pagination/grid_cards?offset=0&limit={total}&sortDirection=ASC&sortField=title&entityType=character")
    to_save = []
    all_c = response.json()
    for chr in all_c["data"]["results"]["data"][:10]:
        link = chr["link"]["link"]
        link2 = f"{MARVER_URL}{link}"
        name = chr["headline"]
        name += chr["secondary_text"] if chr["secondary_text"] is not None else ""
        char_response = req.get(f"{MARVER_URL}{link}")
        html = char_response.content
        soup = BeautifulSoup(html, "lxml")
        data_dict = []
        data_dict.append(name)
        data_dict.append(link2)
        print(link2)
        try:
            accordion = soup.find("div", attrs={"class": "RailExploreBio__Accordion"})

            lable = accordion.find_all("p", attrs={"class": "RailExploreBio__Info__Label"})
            stat = accordion.find_all("li", attrs={"class": "RailExploreBio__Info__Stat"})

            for al, s in zip(lable, stat):
                data_dict.append(s.text)
        except AttributeError:
            data_dict.extend([name, link, "NO DATA"])

        to_save.append(data_dict)

        with open("test.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(to_save)