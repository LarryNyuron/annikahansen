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
def AnnounceParser(): #Копирует ссылки на продажу и создает файл с ссылками в ряд
    f = open('UrlList.txt','w')
    for all_h1 in AI.find_all('div', class_='list-container'):
        for href in all_h1('a'):
           gethref.append('https://www.gazpromnoncoreassets.ru/' + href.get('href'))
    f.write("\n".join(map(str,set(gethref))))
    f.close()

AnnounceParser()


def UrlPicker(): #Отбирает ссылку по запросу для перехода на другой URL
    global url
    list = []
    file = open('UrlList.txt')
    for i in file:
        list.append(i)
    num = list[int(input('номер: '))]
    url = ""f'{num}'""
    print(url)
    file.close()

UrlPicker()






