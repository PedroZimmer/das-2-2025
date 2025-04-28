import boto3
import time

dynamodb = boto3.client('dynamodb', region_name='us-east-1')


try:
    start_time = time.time()
    response = dynamodb.get_item(
        TableName='cliente',
        Key={
            'cpf': {'S': '12345678900'}
        }
    )
    end_time = time.time()

    execution_time = end_time - start_time
    print(f"Tempo de execução da query: {execution_time:.6f} segundos")

    if "Item" in response:
        item = response['Item']
        print(f"Item encontrado: {item}")
except Exception as e:
    print(e)
