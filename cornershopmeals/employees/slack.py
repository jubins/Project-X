from requests import request
from configparser import ConfigParser
from celery import shared_task

env = ConfigParser()
env.read('../env.ini')

SLACK_WEBHOOK_URL = env['slack'].get('WEBHOOK_URL')


@shared_task
def send_slack_message(message):
    headers = {
        'Content-type': 'application/json',
    }
    data = '{"text":"' + message + '"}'
    response = request(method='POST', url=SLACK_WEBHOOK_URL, headers=headers, data=data)
    return response.text


print(send_slack_message('Hello World!'))





