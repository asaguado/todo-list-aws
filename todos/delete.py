import os
import boto3
from todoTableClass import todoTable

dynamodb = boto3.resource('dynamodb')


def delete(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    
    id_var = event['pathParameters']['id']

    # delete the todo from the database
    todoTable.delete_todo(id_var,table)

    # create a response
    response = {
        "statusCode": 200
    }

    return response
