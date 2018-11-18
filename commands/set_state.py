from jira import JIRA


import command_system
from settings import server, basic_auth, project


def set_state(body, chat_id, user_id):
    
    jira = JIRA(server, basic_auth=basic_auth)
    
    answer = ''

    body = body.split()

    
    if body[1].startswith(project['key'].lower()):
        task = body[1]
        state = body[2] + '1'

    elif body[2].startswith(project['key'].lower()):
        task = body[2]
        state = body[1] + '1'

    else:
    	'Нет такой задачи'

    try:
        issue = jira.issue(task)
        jira.transition_issue(issue, state)
    except:
        return 'Нет такого статуса или задачи'
    return 'Статус задачи успешно изменен'



sets = command_system.Command()

sets.keys = ['!setstate', '!set_state', '!set']
sets.process = set_state
sets.description = 'Изменение текущего состояния задачи (1 - к выполнению, 2 - в работе, 3 - готово)'