import boto3


def create_dynamodb_table(table_name: str, id_field_name: str):
    db_client = boto3.client('dynamodb')
    if table_name not in db_client.list_tables()['TableNames']:
        db_client.create_table(AttributeDefinitions=[{'AttributeName': id_field_name, 'AttributeType': 'S'}],
                               TableName=table_name,
                               KeySchema=[{'AttributeName': id_field_name, 'KeyType': 'HASH'}],
                               ProvisionedThroughput={'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5})
    waiter = db_client.get_waiter('table_exists')
    waiter.wait(TableName=table_name)
    return boto3.resource('dynamodb').Table(table_name)
