# S3 helpers using boto3
import boto3

def get_s3_client(endpoint_url, access_key, secret_key):
    return boto3.client(
        's3',
        endpoint_url=endpoint_url,
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key
    )
