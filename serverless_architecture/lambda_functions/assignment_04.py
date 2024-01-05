import boto3
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def lambda_handler(event, context):
    
    s3 = boto3.client('s3')
    buckets = s3.list_buckets()

    for bucket in buckets['Buckets']:
        bucket_name = bucket['Name']
        try:
            encryption = s3.get_bucket_encryption(Bucket=bucket_name)
            # Assuming if the call succeeds, the bucket is encrypted
            logger.info(f'Bucket {bucket_name} is encrypted.')

        except s3.exceptions.ClientError as e:
            # If the call fails, the bucket might not be encrypted
            error_code = e.response['Error']['Code']
            if error_code == 'ServerSideEncryptionConfigurationNotFoundError':
                logger.warning(f'Bucket {bucket_name} is not encrypted.')
