from audioop import add
from src.kfc import get_5050, coupons, coupons_search
from src.audio_parser import parse_audio, add_audio

from vkbottle.bot import Blueprint, Message, rules
from vkbottle_types.objects import MessagesConversation
from random import randrange, choice
import asyncio
import json


class ChatInfoRule(rules.ReplyMessageRule):
    async def check(self, message: Message) -> dict:
        chats_info = await bp.api.messages.get_conversations_by_id(message.peer_id)
        return {'chat': chats_info.items[0]}


class music():
    def __init__(self):
        with open('json_data/music.json', 'r', encoding='utf-8') as read_file:
            self.music_json = json.load(read_file)

    def upd(self):
        with open('json_data/music.json', 'r', encoding='utf-8') as read_file:
            self.music_json = json.load(read_file)


session_chat_jopa = {}

# Получение темплейтов
with open('json_data/answers.json', 'r', encoding='utf-8') as read_file:
    intents = json.load(read_file)

with open('json_data/chats.json', 'r', encoding='utf-8') as read_file:
    chats_json = json.load(read_file)

music_json = music()


bp = Blueprint('for chat commands')
bp.labeler.vbml_ignore_case = True
bp.labeler.auto_rules = [ChatInfoRule()]


@bp.on.message(text='добавь')
async def add_data(message: Message):
    
    for attachment in message.attachments:

        if attachment.audio != None:
            await add_audio(f'{attachment.audio.owner_id}_{attachment.audio.id}', f'{attachment.audio.artist} - {attachment.audio.title}')
            music_json.upd()
            await message.answer('трек добавлен')

        elif attachment.link != None:
            await parse_audio(attachment.link.url)
            music_json.upd()
            await message.answer('плейлист добавлен')

        elif attachment.photo != None:
            print(attachment.photo, '\n\n')


@bp.on.chat_message(text='<msg>')
async def chat_resp(message: Message, chat: MessagesConversation, msg):
    await response(message, msg, chat)


@bp.on.private_message(text='<msg>')
async def private_resp(message: Message, msg):
    await response(message, msg)


async def response(message, msg, chat=None):

    respns = msg.lower()
    peer_id = chat.peer.id if chat != None else message.peer_id
    check = False
    flag = 0
    
    if respns == 'жопа':

        if session_chat_jopa == {}:
            session_chat_jopa[f'chat_{peer_id}'] = 0

        elif f'chat_{peer_id}' not in session_chat_jopa.keys():
            session_chat_jopa[f'chat_{peer_id}'] = 0

        if session_chat_jopa[f'chat_{peer_id}'] < 4:
            session_chat_jopa[f'chat_{peer_id}'] += 1
            await message.answer('ахахах')

        else:
            await message.answer('АХАХАХ')
            session_chat_jopa[f'chat_{peer_id}'] = 0

        return

    elif respns in ['5050', '5050 давай', 'wednesday']:
        await message.answer(await get_5050())
        return

    elif respns in ['ебани купоны', 'купоны', 'акцыи кефас']:
        for msg in await coupons():
            await message.answer(msg)
        return

    elif respns[:4].lower() == 'хочу':
        for msg in await coupons_search(respns[5:].lower()):
            await message.answer(msg)
        return

    elif 'рандом' == respns:
        flag = 1

    elif 'трек' == respns:
        if len(music_json.music_json['music']) > 0:
            random_audio = choice(music_json.music_json['music']).get('track_id')
            await message.answer(attachment=f'audio{random_audio}')
            return
        
        else:
            await message.answer('треков-то нет')
            return

    elif 'жараж' in respns or 'жаров' in respns:
        pic_url = 'photo-191163480_457239027'
        await message.answer(attachment=pic_url)
        await asyncio.sleep(3)

    for intent in intents['intents']:
        for pattern in intent['patterns']:

            if pattern in respns:
                #------------------------Ответ текстом-----------------------------------------
                if intent['type'] == 'text':

                    if intent['word'] == True:

                        if respns == pattern:

                            message_out = intent['response']
                            await message.answer(message_out)

                    else:

                        message_out = intent['response']
                        await message.answer(message_out)

                    check = True
                #------------------------------------------------------------------------------

                #------------------------Ответ картинкой---------------------------------------
                elif intent['type'] == 'photo':

                    if intent['word'] == True:

                        if respns == pattern:

                            pic_url = intent['response']
                            await message.answer(attachment=pic_url)

                    else:

                        pic_url = intent['response']
                        await message.answer(attachment=pic_url)

                    check = True
                #------------------------------------------------------------------------------

                #------------------------Ответ рандомной картинкой из нескольких---------------
                elif intent['type'] == 'one of many (pic)':
                    
                    quantity = int(intent['quantity'])
                    tmp = randrange(0, quantity, 1)
                    
                    if intent['word'] == True:
                        
                        if respns == pattern:
                            
                            pic_url = intent['response'][tmp]
                            dicpic = pic_url
                            await message.answer(attachment=pic_url)
                    
                    else:
                        
                        pic_url = intent['response'][tmp]
                        dicpic = pic_url
                        await message.answer(attachment=pic_url)

                    check = True
        if check:
            break
                #------------------------------------------------------------------------------

    if flag == 1:

        if dicpic == 'photo-191163480_457239025':

            await asyncio.sleep(2)
            await message.answer( 'photo-191163480_457239184')

        flag = 0
        dicpic = None
