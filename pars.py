import os
import importlib

from command_system import command_list


def load_modules():
    ''' Подгрузка модулей с командами'''
    files = os.listdir("commands")

    modules = filter(lambda x: x.endswith('.py'), files)
    
    for m in modules:
        importlib.import_module("commands." + m[0:-3])


def parse(body, chat_id, user_id):
    ''' Парсинг строки на команды наличие команды '''
    body = body.lower()
    
    list = body.split()

    load_modules()

    answer = ''

    if body[0] != '!':
        return answer

    for command in command_list:
        if list[0] in command.keys:
            answer = command.process(body, chat_id, user_id)
            break

    return answer
