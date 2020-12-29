from requests import request
from celery import shared_task
from configparser import ConfigParser

env = ConfigParser()
env.read('env.ini')

SLACK_WEBHOOK_URL = env['slack'].get('WEBHOOK_URL')


@shared_task
def send_slack_message(message):
    headers = {
        'Content-type': 'application/json',
    }
    data = '{"text":"' + message + '"}'
    response = request(method='POST', url=SLACK_WEBHOOK_URL, headers=headers, data=data)
    return response







