import boto3
import time
import uuid
from botocore.exceptions import ClientError

def test(dynamodb, v_text):
    '''
    How To Add Data to Amazon DynamoDB
    https://www.bmc.com/blogs/dynamodb-adding-data/
    '''
    
    table = dynamodb.Table('todoTable')

    timestamp = str(time.time())
    
    item = {
        'id': str(uuid.uuid1()),
        'text': v_text,
        'checked': False,
        'createdAt': timestamp,
        'updatedAt': timestamp,
    }
    print(item)
    
    timestamp = str(time.time())

    try:
        response = table.put_item(Item=item)
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print(response)
        return response  


if __name__ == '__main__':
    dynamodb = boto3.resource('dynamodb',  endpoint_url = "http://localhost:8000")
    test(dynamodb,"Hola mundo")