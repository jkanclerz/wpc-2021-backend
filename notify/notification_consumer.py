import boto3
import os
import random
import json
from notificator import notify


QUEUE_URL = os.getenv('QUEUE_URL')
sqs = boto3.resource('sqs')

notifications = sqs.Queue(QUEUE_URL)

while True:
    for msg in notifications.receive_messages(WaitTimeSeconds=10):
        
        my_request = json.loads(msg.body)
        notify(my_request)
        msg.delete()