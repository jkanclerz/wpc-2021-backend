import boto3
import os
import json

def handle_order(order_request):
    sqs = boto3.resource('sqs')
    orders_to_be_processed = sqs.Queue(os.getenv('QUEUE_ORDERS'))
    orders_to_be_processed.send_message(
        MessageBody=json.dumps(order_request)
    )