import boto3
import time
import uuid
from botocore.exceptions import ClientError

def test(event, context):
    '''
    How To Add Data to Amazon DynamoDB
    https://www.bmc.com/blogs/dynamodb-adding-data/
    '''
    print(":: paso por aqui 1")
    dynamodb = boto3.resource('dynamodb', endpoint_url = "http://localhost:8000")
    table = dynamodb.Table('todoTable')

    timestamp = str(time.time())
    
    item = {
        'id': str(uuid.uuid1()),
        'text': "Hola mundo",
        'checked': False,
        'createdAt': timestamp,
        'updatedAt': timestamp,
    }
    print(item)
    timestamp = str(time.time())

    try:
        print(":: paso por aqui 2")
        print(table)
        response = table.put_item(Item=item)
        print(response)
    except ClientError as e:
        print(":: paso por aqui 3")
        print(e.response['Error']['Message'])
    except:
        print(":: paso por aqui 4")        
        print(":: Something went wrong")
        print(e.response['Error']['Message'])
    else:
        print(":: paso por aqui 5")
        print(response)
        return response  