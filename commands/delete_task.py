from jira import JIRA


import command_system
from settings import server, basic_auth, admin_ids, project


def delete_task(body, chat_id, user_id):

    if user_id not in admin_ids:
        return 'У вас нет прав доступа'

    jira = JIRA(server, basic_auth=basic_auth)
    
    body = body.split()

    if not body[1]:
        return 'Неверный ввод'

    if body[1] == 'all':
        for issue in jira.search_issues('project='+project['key']):
            issue.delete()
        return 'All tasks deleted'

    try:
        issue = jira.issue(body[1])
        issue.delete()

    except:
        return 'Такая задача не существует'

    return "Task deleted"


test_command = command_system.Command()

test_command.keys = ['!deletetask', '!delete_task']
test_command.process = delete_task
test_command.description = 'Удаление задачи JIRA по её имени (только для администратора бота)'