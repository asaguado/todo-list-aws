import json

def lambda_handler(event, context):
    # TODO implement
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Test LambdaFunction",
            # "location": ip.text.replace("\n", "")
        }),
    }