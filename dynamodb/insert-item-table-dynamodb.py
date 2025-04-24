import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.client('dynamodb', region_name='us-east-1')

items = [
    {
        'cpf': {'S': '12345678900'},
        'nome': {'S': 'João da Silva'},
        'clienteativo': {'S': 'true'},
    },
    {
        'cpf': {'S': '98765432100'},
        'nome': {'S': 'Maria Oliveira'},
        'clienteativo': {'S': 'false'},
    },
    {
        'cpf': {'S': '11122233344'},
        'nome': {'S': 'Carlos Pereira'},
        'clienteativo': {'S': 'true'},
    },
]

for item in items:
    try:
        dynamodb.put_item(
            TableName='cliente',
            Item=item
        )
        print(f"Item {item['cpf']['S']} inserido com sucesso.")
    except ClientError as e:
        print(f"Erro ao inserir item {item['cpf']['S']}: {e.response['Error']['Message']}")