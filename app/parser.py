import requests
from bs4 import BeautifulSoup


def get_html(url):
    result = requests.get(url)
    return result.text


def get_grechka():
    html = get_html('https://rozetka.com.ua/ua/199607923/p199607923/')
    soup = BeautifulSoup(html, 'lxml')
    section = soup.find('p', {'class': 'product-prices__big'})
    cost = section.text
    grecha = ''.join(str(s) for s in cost if s.isnumeric())
    return int(grecha)


def get_siga():
    html = get_html('https://fozzyshop.com.ua/sigarety/56828-sigareti-winston-xs-plus-duo-4820000535786.html')
    soup = BeautifulSoup(html, 'lxml')
    section = soup.find('span', {'class': 'current-price'})
    cost = section.text
    siga = ''.join(str(s) for s in cost if s.isnumeric())
    siga = siga[0:2]
    return int(siga)


def get_water():
    html = get_html("https://rozetka.com.ua/ua/karpatska_djerelna_4820051240530/p38885232/")
    soup = BeautifulSoup(html, 'lxml')
    section = soup.find('span', {'class': 'recount__accent'})
    cost = section.text
    water = ''.join(str(s) for s in cost if s.isnumeric())
    water = water[0:2]
    return int(water) / 6
