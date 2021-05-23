import json
import os
import boto3
import logging
import time
import uuid
from todoTableClass import todoTable



def create(event, context):
    
    dynamodb = boto3.resource(
        'dynamodb', endpoint_url="http://localhost:8000")   
        
    data = json.loads(event['body'])
    if 'text' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't create the todo item.")
    
    timestamp = str(time.time())

    table_name = os.environ['DYNAMODB_TABLE']
    table = dynamodb.Table(table_name)
    print(":: table_name: " + str(table_name))
    print(table)

    item = {
        'id': str(uuid.uuid1()),
        'text': data['text'],
        'checked': False,
        'createdAt': timestamp,
        'updatedAt': timestamp,
    }
    id_var = str(uuid.uuid1())
    text_var = data['text']
    print(":: id_var: " + str(id_var))
    print(":: text_var: " + str(text_var))

    # write the todo to the database
    # todoTable.put_todo(text_var,id_var,table)
     # write the todo to the database
    table.put_item(Item=item)

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }

    return response
