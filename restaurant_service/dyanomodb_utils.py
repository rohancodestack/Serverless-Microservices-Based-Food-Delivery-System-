import boto3

dynamodb = boto3.resource('dynamodb')

def save_to_dynamodb(table_name, item):
    table = dynamodb.Table(table_name)
    table.put_item(Item=item)

def get_item_from_dynamodb(table_name, key):
    table = dynamodb.Table(table_name)
    response = table.get_item(Key=key)
    return response.get("Item")