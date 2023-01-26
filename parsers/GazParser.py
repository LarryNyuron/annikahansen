import requests
from bs4 import BeautifulSoup
import json
import csv
import datetime
import time


def get_data():

    url = 'https://www.gazpromnoncoreassets.ru/auctions/form/nedvizhimoe-imushchestvo/filters/all/'

    #current_time = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M")

    with open(f"gazprom.csv", "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            (
               'Title',
               'Region',
               'Url',
               'Min_price'
            )
        )

    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, "lxml")
    land_items = soup.find_all("div", class_="item")
    land_data = []
    for item in land_items:
        land_title = item.find('div', class_='content').find('div', class_='body').h3.a.contents[0]
        land_region = item.find('span', class_='region').contents[0]
        land_href = item.find('div', class_='content').find('div', class_='body').h3.a['href']
        land_info = ' '.join(map(str, item.find('div', class_='info')))
        land_data.append(
            {
                'land_title': land_title,
                'land_region': land_region,
                'land_href': land_href,
                'land_info': land_info
            }
        )
        with open(f"gazprom.csv", "a", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
                (
                    land_title,
                    land_region,
                    land_href,
                    land_info
                )
            )

    pages_count = int(soup.find("li", class_="last").text)
    print(f"Обработана 1/{pages_count}")
    for page in range(2, pages_count + 1):
        url = f'https://www.gazpromnoncoreassets.ru/auctions/form/nedvizhimoe-imushchestvo/page/{page}/filters/all/'

        response = requests.get(url=url)
        soup = BeautifulSoup(response.text, "lxml")

        land_items = soup.find_all("div", class_="item")
        land_data = []
        for item in land_items:
            land_title = item.find('div', class_='content').find('div', class_='body').h3.a.contents[0]
            land_region = item.find('span', class_='region').contents[0]
            land_href = item.find('div', class_='content').find('div', class_='body').h3.a['href']
            land_info = ' '.join(map(str, item.find('div', class_='info')))
            land_data.append(
                {
                    'land_title': land_title,
                    'land_region': land_region,
                    'land_href': land_href,
                    'land_info': land_info
                }
            )
            with open(f"gazprom.csv", "a", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(
                    (
                        land_title,
                        land_region,
                        land_href,
                        land_info
                    )
                )
        print(f"Обработана {page}/{pages_count}")
        time.sleep(1)


def main():
    get_data()



if __name__ == '__main__':
    main()