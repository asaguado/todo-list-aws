import json
import os
import boto3
import logging
from todos import decimalencoder
from todoTableClass import todoTable
dynamodb = boto3.resource('dynamodb')


def get(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    
    id_var = event['pathParameters']['id']

    # fetch todo from the database
    result = todoTable.get_todo(id_var, table)
    print('::Result: '+str(result))
    
    if not 'Item' in result:
        print('::Get Failed')
        logging.error("Get Failed")
        raise Exception("Couldn't find the todo item.")
        return 

    try:
        print('::Get OK')
        # create a response
        response = {
            "statusCode": 200,
            "body": json.dumps(result['Item'],
                           cls=decimalencoder.DecimalEncoder)
        }
        return response
        
    except:
        print('::Get Failed')
        logging.error("Get Failed")
        raise Exception("Couldn't find the todo item.")
        return
