import requests
from bs4 import BeautifulSoup
from json import loads


# КЕКВ акции 5050
async def get_5050():
    try:
        page = requests.get('https://www.kfc.ru/promo/crazydays/').text
        soup = BeautifulSoup(page, 'html.parser')

        text = soup.find('h1').text
        date = soup.find('p').text[0:30]

        return text + '\n' + date

    except:
        return 'сорямба, я ещё не знаю, что там будет'


# да тут ещё и купоны есть, ало
async def coupons():

    response = loads(requests.get(
        'https://api.kfc.com/api/menu/api/v1/menu.short/74021825/website/finger_lickin_good'
    ).text)

    msg = []

    for coupon in response['value']['products'].values():
        if coupon['type'] == 'Combo':
            if 'купон' in coupon['title'].lower():

                title = coupon['title']
                price = str(int(int(coupon['price'])/100)) + ' деревянных'
                desc = coupon['descr']

                msg.append(title + '\n' + price + '\n' + desc)

    return msg


# с поиском ёмана
async def coupons_search(search_phrase):

    response = loads(requests.get(
        'https://api.kfc.com/api/menu/api/v1/menu.short/74021825/website/finger_lickin_good'
    ).text)
    
    msg = []

    for coupon in response['value']['products'].values():
        if coupon['type'] == 'Combo':
            if ('купон' in coupon['title'].lower() and (search_phrase in coupon['title'].lower() or search_phrase in coupon['descr'].lower())):

                title = coupon['title']
                price = str(int(int(coupon['price'])/100)) + ' деревянных'
                desc = coupon['descr']
                
                msg.append(title + '\n' + price + '\n' + desc)

    return msg if msg != [] else ['нет такого :с']
