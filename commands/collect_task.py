import requests
import json

from jira import JIRA

import command_system
from settings import server, basic_auth, project



def collect_task(body, chat_id, user_id):
    
    jira = JIRA(server, basic_auth=basic_auth)
    
    answer = ''
    
    checker = lambda x: x.name if x else 'отсутствует'

    body = body.split()

    if len(body) == 1 or body[1] == 'all':

        issues_in_proj = jira.search_issues('project='+project['key'])

        for issue in issues_in_proj:
            answer += '{} : {} \nИсполнитель: {}\nСтатус: {}\n'.\
                       format(issue.key, issue.fields.summary,
                       checker(issue.fields.assignee),
                       issue.fields.status)

    else:
        try:
            issue = jira.issue(body[1])
            answer = '{} : {} \nИсполнитель: {}\nСтатус: {}\n'.\
                      format(issue.key, issue.fields.summary,
                      checker(issue.fields.assignee),
                      issue.fields.status)
        except:
            return 'Нет такой задачи'

    return answer



test2_command = command_system.Command()

test2_command.keys = ['!collect', '!collecttask', '!collect_task']
test2_command.process = collect_task
test2_command.description = 'Список текущих задач JIRA'