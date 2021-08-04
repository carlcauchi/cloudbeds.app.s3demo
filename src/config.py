import boto3
import os
 
# creating the aws s3 client
# as a standard practice we are not hard-coding the aws access key id and secret key credentials here
# the credentials are defined as environment variables
def create_s3_client():
    return boto3.client(
        's3',
        aws_access_key_id=os.environ.get('AWS_KEY_ID', 'aws-key-not-set'), 
        aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY', 'aws-secret-access-key-not-set'), 
        region_name=os.environ.get('AWS_REGION_NAME', 'aws-region-not-set')
    )