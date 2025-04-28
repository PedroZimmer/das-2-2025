import boto3

dynamodb = boto3.client('dynamodb', region_name='us-east-1')

try:
    response = dynamodb.scan(
        TableName="cliente",
        FilterExpression="clienteativo = :val1",
        ExpressionAttributeValues={
            ':val1': {'S': 'true'}
        }
    )

    if 'Items' in response:
        for item in response['Items']:
            print(f"Item encontrado: {item}")
except Exception as e:
    print("Erro ao escanear os itens:", e)