import json
import os
import boto3
import logging
import time
import uuid
from botocore.exceptions import ClientError
from todoTableClass import todoTable


dynamodb = boto3.resource('dynamodb', endpoint_url = "http://localhost:8000")


def create(event, context):
    '''
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
    print(":: table_status: " + str(table.table_status))

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
    print(":: paso por aqui 1")    
    table.put_item(Item=item)
    print(":: paso por aqui 2")    
    print(table)

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }
    print(response)

    return response
    '''

    table = dynamodb.Table('todoTable')
    timestamp = str(time.time())
    #print(table.item_count)
    print("::create.py::")
    data = json.loads(event['body'])
    print(data)     
    item = {
        'id': str(uuid.uuid1()),
        'text': data['text'],
        'checked': False,
        'createdAt': timestamp,
        'updatedAt': timestamp,
    }
    print("::id: "+str(uuid.uuid1()))
    print("::test: "+data['text'])    
    print(item)
    print(":: paso por aqui 1")
    try:
        print(":: paso por aqui 2")
        response = table.put_item(Item=item)
        print(":: paso por aqui 3")
        print(response)
        
    except ClientError as e:
        print(":: paso por aqui 4")
        print(e.response['Error']['Message'])
        
    else:
        print(":: paso por aqui 5")
        print(response)
        return response
