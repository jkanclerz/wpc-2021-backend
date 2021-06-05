import json
from notificator import notify

def lambda_handler(event, context): 

    for message in event['Records']:
        notification_request = json.loads(message['body'])
        notify(notification_request)


    return {
        'statusCode': 200,
        'body': 'OK'
    }
