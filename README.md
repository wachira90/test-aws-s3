# test-aws-s3
test-aws-s3 python

main.py

```
#!python
import boto3

s3 = boto3.client('s3', aws_access_key_id='xxxx', aws_secret_access_key='xxxxx')

bucket_name = 'oms-dev-storage'
# prefix = 'your-folder-name/'
prefix = '/'

response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)

for obj in response['Contents']:
    print(obj['Key'])
```

result

```
(env) D:\test\python\fda-s3>python main.py
D:\test\python\fda-s3\env\lib\site-packages\boto3\compat.py:82: PythonDeprecationWarning: Boto3 will no longer support Python 3.7 starting December 13, 2023. To continue receiving service updates, bug fixes, and security updates please upgrade to Python 3.8 or later. More information can be found here: https://aws.amazon.com/blogs/developer/python-support-policy-updates-for-aws-sdks-and-tools/
  warnings.warn(warning, PythonDeprecationWarning)
/data/user/0/cache/11932fd5-2896-440c-8bf0-972300029c90/IMG-20230821-WA0020.jpg
/data/user/0/cache/4b1dd19c-b8fc-4fe1-9bd7-7de9bed41361/37238-4-sitting-man-image (1).png
/data/user/0/cache/6cd504bc-0af4-412c-96b1-2ca9d578856a/IMG-20230815-WA0001.jpg
/data/user/0/cache/8c3d5829-e558-4394-b2af-91bd41d8d003/37238-4-sitting-man-image (1).png
/data/user/0/cache/ab659f49-611f-4ac1-8bf7-15040c585a2f/37238-4-sitting-man-image (1).png
/data/user/0/cache/dde03121-9f6e-4359-b3bc-14383fdf6a98/IMG-20230820-WA0004.jpg
/data/user/0/com.finansia.finansia_crypto/cache/de74f5e9-5399-44eb-85e4-a857e55973c6/IMG-20230821-WA0023.jpg
```


