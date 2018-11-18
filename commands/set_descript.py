from jira import JIRA


import command_system
from settings import server, basic_auth, project


def change_description(body, chat_id, user_id):
    
    jira = JIRA(server, basic_auth=basic_auth)
    
    answer = ''

    body = body.split()
    
    checker = lambda x, i, j: x[i:j] if len(x)-1 >= i else None 

    task = checker(body,i, i+1)

    if len(body) > 2:
        body = ' '.join(body[2:])
    else:
    	body = ''
    
    try:
        issue = jira.issue(task)
        issue.update(description=body)
    except:
        return 'Нет такой задачи'

    return 'Описание задачи успешно изменено'



sets = command_system.Command()

sets.keys = ['!setdes', '!set_des']
sets.process = change_description
sets.description = 'Изменение описания задачи (usage: !setdes "issues" description)'