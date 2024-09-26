import boto3

# Авторизация
s3 = boto3.client(
    service_name='s3',
    endpoint_url='https://s3.ru-1.storage.selcloud.ru',
    region_name='ru-1',
    aws_access_key_id='#',
    aws_secret_access_key='#'
)

# Создание бакета
bucket_name = "bucket_AWS_SDK_Python"

try:
    s3.create_bucket(Bucket=bucket_name)
    print(f"Бакет '{bucket_name}' успешно создан.")
except Exception as e:
    print(f"Ошибка при создании бакета: {e}")
