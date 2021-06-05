import json
from ordering import handle_order
import uuid

def lambda_handler(orderRequest, context):

    if not 'photos' in orderRequest:
        raise Exception("invalid request, missing photos list")
    
    if not 'email' in orderRequest:
        raise Exception("invalid request, missing email")

    if len(orderRequest['photos']) <= 1:
        raise Exception("not enough photos selected")

    orderRequest["request_id"] = str(uuid.uuid4())

    handle_order(orderRequest)

    return {
        'statusCode': 200,
        'body': 'Your order is being processed'
    }
