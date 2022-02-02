from json import dump
import requests
from pyshorteners import Shortener
from bs4 import BeautifulSoup
from random import choice


def get_news():
    try:
        link = 'https://www.google.com/search?q=%D0%BD%D0%BE%D0%B2%D0%BE%D1%81%D1%82%D0%B8+%D1%83%D0%BA%D1%80%D0%B0%D0%B8%D0%BD%D0%B0&rlz=1C1GCEU_ruRU917RU918&source=lnms&tbm=nws&sa=X&ved=2ahUKEwjJnoun99v1AhUOvYsKHXorAzoQ_AUoAXoECAEQAw&biw=1517&bih=694&dpr=0.9'
        
        page = requests.get(link).text
        soup = BeautifulSoup(page, 'html.parser')

        news = soup.find_all('div', {'class':'ZINbbcxpd', 'class':'xpd'})
        item = choice(news)

        header = item.find('div', {'class': 'vvjwJb'}).text
        body = item.find('div', {'class': 's3v9rd'}).text
        img = item.find('img')['src']

        shrt = Shortener()
        source = shrt.tinyurl.short('google.com' + item.find('a')['href'])
            
        
        return [header, body, source, img]

    except:

        return get_news()
