import json
import boto3
import os
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return int(o)
        return super(DecimalEncoder, self).default(o)

def lambda_handler(event, context):
    try:
        response = table.update_item(
            Key={'id': 'visitor'},
            UpdateExpression="ADD visit_count :inc",
            ExpressionAttributeValues={':inc': 1},
            ReturnValues="UPDATED_NEW"
        )
        count = response['Attributes']['visit_count']

        # API Gateway HTTP API automatically adds CORS headers from its config,
        # so we don't need to set Access-Control-Allow-Origin here.
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'count': count}, cls=DecimalEncoder)
        }
    except Exception as e:
        print(f"Error: {e}")
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'error': 'Internal Server Error'})
        }