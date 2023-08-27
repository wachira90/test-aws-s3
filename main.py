#!python
import boto3

s3 = boto3.client('s3', aws_access_key_id='xxxx', aws_secret_access_key='xxxx')

bucket_name = 'oms-dev-storage'
# prefix = 'your-folder-name/'
prefix = '/'

response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)

for obj in response['Contents']:
    print(obj['Key'])
