from settings import token, whitelist, admin_ids
import command_system

def add_chat(body, chat_id, user_id):
    '''Добавление id чата в вайт лист'''
    if user_id not in admin_ids: 
        return 'Вы не имеете прав администратора'
    
    try:
        id = int(body.split()[1])
    except:
    	return 'Неправильный формат команды'

    file = open(whitelist, 'a')
    file.write(str(id) + '\n')
    file.close()
    return 'Чат добавлен'



test_command = command_system.Command()

test_command.keys = ['!add_chat', '!добавить_чат', '!addchat']
test_command.process = add_chat
test_command.description = 'добавление чата в whitelist(только для администратора бота)'