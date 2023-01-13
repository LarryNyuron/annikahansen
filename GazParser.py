import requests
from bs4 import BeautifulSoup


url = 'https://www.gazpromnoncoreassets.ru/auctions/purpose/proizvodstvennye-sklady-i-bazy/auctiontype/announces/"


def SiteSaver(url):
    '''
    Функция сохраняет сайт,чтоб не забанили
    '''
    req = requests.get(url)
    src = req.text
    with open('index.html', 'w') as file:
        file.write(src)

SiteSaver()

with open('index.html') as file:
    src = file.read()

AI = BeautifulSoup(src,'lxml')


ImgList = []
def ImgParser():    #Функция парсит картинки с сайта
    AllInfo = AI.find_all('div', class_='thumb')
    all_img = []
    for i in AllInfo:
        all_img.append(i.img['src'])
        for i in all_img:
            ImgList = ('https://www.gazpromnoncoreassets.ru/' + i)
        print(ImgList)


gethref = []
def AnnounceParser(): #Копирует ссылки на продажу и создает файл с ссылками в ряд
    f = open('UrlList.txt','w')
    all_href = AI.find_all('h3', class_='title')
    for i in all_href:
        a = i.find('a')
        gethref = a.get('href')
    print(gethref)


    f.write("\n".join(map(str,gethref)))
    #print("\n".join(map(str,gethref)))
    f.close()
AnnounceParser()

TitleLine = []
def GetTitile(): #Выдает названия лотов
    title = AI.find_all('h3', class_='title')
    for i in title:
        TitleLine.append(i.text)
    TitleLine.pop(0)

"""
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

def SiteSaver2():   #Функция сохраняет сайт, шоб не забанили
    req = requests.get(url)
    src = req.text
    with open('index2.html', 'w') as file:
        file.write(src)

SiteSaver2()

"""
