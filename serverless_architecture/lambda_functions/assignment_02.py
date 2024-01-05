import boto3
import logging
from datetime import datetime, timezone

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def lambda_handler(event, context):
    bucket_name = 'leftattention-hero-assignments'
    s3 = boto3.client('s3')

    # Get the current date
    current_time = datetime.now(timezone.utc)

    objects = s3.list_objects_v2(Bucket=bucket_name)

    if 'Contents' in objects:
        for obj in objects['Contents']:
            creation_time = obj['LastModified']

            # Calculate the difference in days
            age_in_days = (current_time - creation_time).days

            # Delete objects older than 30 days
            if age_in_days > 30:
                s3.delete_object(Bucket=bucket_name, Key=obj['Key'])
                logger.info(f'Deleted {obj["Key"]}')
