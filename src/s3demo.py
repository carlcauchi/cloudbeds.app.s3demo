import os

from botocore.exceptions import ClientError
 
from config import create_s3_client
 
# bucket name
# note - we are considering that the bucket already exists in the aws environment.
# we can have a check_bucket function() to check whether the bucket exists or not
BUCKET = os.environ['AWS_BUCKET_NAME']
 
# s3 client instance to perform the s3 related operations
s3_client = create_s3_client()
 
 
# get the list of files from s3 bucket
def list_files():
    contents = []
    try:
        response = s3_client.list_objects_v2(Bucket=BUCKET)
        if 'Contents' in response:
            for item in response['Contents']:
                # print(item)
                contents.append(item)
        else:
            print('Bucket is empty')
    except ClientError as e:
        print(e)
 
    return contents

# application healthcheck
def health_check():
    try:
        response = '{"status": "ok"}'
    except ClientError as e:
        print(e)

    return response