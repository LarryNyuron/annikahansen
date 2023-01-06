import requests
from bs4 import BeautifulSoup

url = "https://www.gazpromnoncoreassets.ru/auctions/purpose/proizvodstvennye-sklady-i-bazy/auctiontype/announces/"
#url = input('Введите ссылку на сайт: ')

def SiteSaver():   #Функция сохраняет сайт, шоб не забанили
    req = requests.get(url)
    src = req.text
    with open('index.html', 'w') as file:
        file.write(src)

SiteSaver()

with open('index.html') as file:
    src = file.read()

AI = BeautifulSoup(src,'lxml')



def ImgParser():    #Функция парсит картинки с сайта
    AllInfo = AI.find_all('div', class_='thumb') 
    all_img = []
    for i in AllInfo:
        all_img.append(i.img['src'])
        for i in all_img:
            print('https://www.gazpromnoncoreassets.ru/' + i)



gethref = []
def AnnounceParser(): #Копирует ссылки на продажу
    for all_h1 in AI.find_all('div', class_='list-container'):
        for href in all_h1('a'):
           gethref.append('https://www.gazpromnoncoreassets.ru/' + href.get('href'))
    print(set(gethref))

AnnounceParser()







