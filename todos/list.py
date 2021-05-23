import json
import os
import boto3
import decimalencoder
from todoTableClass import todoTable


dynamodb = boto3.resource('dynamodb', endpoint_url="http://127.0.0.1:8000")


def list(event, context):
    
    '''
    dynamodb = boto3.resource('dynamodb')
    if not dynamodb:
        dynamodb = boto3.resource(
            'dynamodb', endpoint_url="http://localhost:8000")
        print(":: not dynamodb")
    #table = dynamodb.Table('todoTable')
    
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    print(":: table_name: " + str(os.environ['DYNAMODB_TABLE']))

    # fetch all todos from the database
    result = todoTable(table,dynamodb).list_todo()

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Items'], cls=decimalencoder.DecimalEncoder)
    }
    
    return response
    '''
    table_name = os.environ['DYNAMODB_TABLE']
    table = dynamodb.Table(table_name)
    print(":: table_name: " + str(table_name))
    print(":: paso por aqui 1")
    # fetch all todos from the database
    result = table.scan()
    print(":: paso por aqui 2")    
    print(result)

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Items'], cls=decimalencoder.DecimalEncoder)
    }

    return response    