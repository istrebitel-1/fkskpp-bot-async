from bs4 import BeautifulSoup
from json import dump, load, loads
from re import compile

import requests


async def add_data(data, filename='json_data/music.json'):

    with open(filename, 'w', encoding='utf-8') as f:
        dump(data, f, indent=4, ensure_ascii=False)

    f.close()


async def add_audio(audio_id, name):

    with open("json_data/music.json", encoding='utf-8') as misc:
        music = load(misc)

    check = False

    for audio in music['music']:
        if audio_id == audio:
            check = True

    if check == False:

        info = {
            'name': name,
            'track_id' : audio_id
        }
        music['music'].append(info)
        await add_data(music)


async def parse_audio(url):

    try:
        html = requests.get(url).text
    except:
        return 'wrong'
    
    soup = BeautifulSoup(html, 'html.parser')
    data = soup.find_all('div', attrs={f'data-audio': {compile(r'.*')}})
    
    for item in data:

        attr_list = loads(item['data-audio'])

        name = attr_list[4] + ' — ' + attr_list[3]
        id = attr_list[15].get('content_id')

        await add_audio(id, name)
    
    return 'success'
