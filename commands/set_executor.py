from jira import JIRA


import command_system
from settings import server, basic_auth, project


def set_executor(body, chat_id, user_id):
    
    jira = JIRA(server, basic_auth=basic_auth)
    
    answer = ''

    body = body.split()


    if body[1].startswith(project['key'].lower()):
        task = body[1]
        executor = body[2]

    elif body[2].startswith(project['key'].lower()):
        task = body[2]
        executor = body[1]
    
    else:
        return 'Неправильно указана задача'
    
    try:
        issue = jira.issue(task)
        issue.update(assignee=executor)
    except:
        return 'Нет такого участника'
    return 'Исполнитель назначен'



execut = command_system.Command()

execut.keys = ['!setexec', '!setexecutor', '!set_executor']
execut.process = set_executor
execut.description = 'Назначение исполнителя'