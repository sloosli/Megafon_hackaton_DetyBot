from jira import JIRA
from tamtam import TamTam

import command_system
from settings import server, basic_auth
from settings import project, token, type_list



def addtask(body, chat_id, user_id):
    
    jira = JIRA(server, basic_auth=basic_auth)

    body = body.split()
    
    try:
        issuetype = type_list[0] # дефолтное значение
    except:
        return 'Пустой settings.type_list'

    try:
        may_be_type = body[1].capitalize()
    except:
        return 'Пустое название задачи'

    if may_be_type in type_list:
        issuetype = may_be_type
        body = ' '.join(body[2:]) 

    else:
        if len(body) > 1:
            body = ' '.join(body[1:])

    print(issuetype, may_be_type, body)
    issue_dict = {'description': 'By DetyBot',
                  'project': project,
                  'summary': body,
                  'issuetype': {'name': issuetype}}

    try:
        issue = jira.create_issue(fields=issue_dict)
    except:
        return 'Ooops something went wrong'

    return 'Task ' + issue.key +' added'

test2_command = command_system.Command()

test2_command.keys = ['!addtask', '!add_task']
test2_command.process = addtask
test2_command.description = 'Добавление задачи в JIRA (usage: !addtask ["type"] "summary")'