import os
import boto3

TEXT_TEMPLATE = '''
Hello {},

Your animation is ready, it could be downloaded here:

{}

Best 
ACME
'''

HTML_TEMPLATE = '''
<div>
    <h4>Hello {}</h4>

    <p>Your animation is ready, it could be downloaded here:</p>
    <a href="{}">download your animation</a>

    <p>
    Best<br/>
    ACME
    </p>
</div>
'''

def send_email(email, video_url):
    SENDER_EMAIL = os.getenv('SENDER_EMAIL')

    client = boto3.client('ses')
    response = client.send_email(
        Source=SENDER_EMAIL,
        Destination={
               'ToAddresses': [email]
        },
        Message={
            'Subject': {
                'Data': 'Hurray, your video is ready!!!!',
                'Charset': 'utf-8'
            },
            'Body': {
                'Text': {
                    'Data': TEXT_TEMPLATE.format(email, video_url),
                    'Charset': 'utf-8'
                },
                'Html': {
                    'Data': HTML_TEMPLATE.format(email, video_url),
                    'Charset': 'utf-8'
                }
            }
        },
        ReplyToAddresses=[SENDER_EMAIL]
    )

    return response['MessageId']



def notify(notification_request):
    if not 'email' in notification_request:
        raise Exception('invalid notification request, missing email')
    
    if not 'video_url' in notification_request:
        raise Exception('invalid notification request, missing video url')

    print("i going to send an email to: {}".format(notification_request['email']))    
    msgId = send_email(notification_request['email'], notification_request['video_url'])
    print("Message sent, id: {}".format(msgId))

if __name__ == '__main__':
    notify({
        'email': os.getenv('SENDER_EMAIL'),
        'video_url': 'https://video/example'
    })