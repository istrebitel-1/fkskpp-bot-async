import json


async def add_data(data, filename='json_data/chats.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    f.close()


async def check_and_save_chats(chatid):
    with open("json_data/chats.json") as chats:
        chats = json.load(chats)

    check = False

    for chat in chats['chats']:
        for ids in chat['id']:
            if chatid == ids:
                check = True

    if check == False:
        temp = chats['chats']
        info = {"id":[chatid]}
        
        temp.append(info)
        add_data(chats)
