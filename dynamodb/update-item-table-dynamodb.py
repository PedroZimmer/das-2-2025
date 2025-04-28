import boto3

dynamodb = boto3.client('dynamodb', region_name='us-east-1')

try:
    response = dynamodb.update_item(
        TableName="cliente",
        Key= {
            'cpf': {'S': '12345678900'}
        },
        UpdateExpression='SET clienteativo = :val1',
        ExpressionAttributeValues={
            ':val1': {'S': 'false'}
        },
        ReturnValues='UPDATED_NEW'
    )
    print(response)
except Exception as e:
    print("Erro ao atualizar o item:", e)