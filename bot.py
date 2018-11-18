#by Бедные лицейские дети

import requests
import time

import tamtam
import pars
from settings import token, whitelist, bot_id
from settings import admin_chat_ids, admin_ids



tt = tamtam.TamTam(token)

def get_chats():
    ''' Получение чатов из "белого" списка '''

    file = open(whitelist, 'r')

    chat_ids = admin_chat_ids.copy()

    for row in file:
        chat_ids.append(int(row))

    file.close()

    return chat_ids



while True:

    chat_ids = get_chats()

    for chat in chat_ids:

        messages = tt.get_messages(chat)[:50]

        for content in messages:

            if content['message']['text']:   

                print(content['message']['text'])
                
                chat_id = content['recipient']['chat_id']
                user_id = content['sender']['user_id']
              
                
                if user_id == bot_id: break
                
                answer = pars.parse(content['message']['text'],
                                    chat_id, user_id)
                if not answer: continue

                tt.send(chat_id, answer)
                if chat_id < 0 and answer.split()[-1] == 'added':
                    tt.send_pers(user_id, answer)
                    tt.send_pers(user_id, ' '.join(content['message']['text'].split()[1:]))

    time.sleep(1)


