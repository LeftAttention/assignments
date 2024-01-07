import boto3
import logging
from datetime import datetime, timezone, timedelta

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def lambda_handler(event, context):
    bucket_name = 'leftattention-public'
    s3 = boto3.client('s3')

    current_time = datetime.now(timezone.utc)

    # List objects in the S3 bucket
    objects = s3.list_objects_v2(Bucket=bucket_name)

    # Check if 'Contents' key is in the response
    if 'Contents' in objects:
        for obj in objects['Contents']:
            # Calculate the age of the file
            age_in_days = (current_time - obj['LastModified']).days

            # Check if the file is older than 6 months (approximately 180 days)
            if age_in_days > 180:
                # Change the storage class of the file to Glacier
                s3.copy_object(
                    Bucket=bucket_name,
                    CopySource={'Bucket': bucket_name, 'Key': obj['Key']},
                    Key=obj['Key'],
                    StorageClass='GLACIER',
                    MetadataDirective='COPY'
                )

                # Log the archived file
                logger.info(f"Archived {obj['Key']} to Glacier")