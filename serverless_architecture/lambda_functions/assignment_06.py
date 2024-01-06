import boto3
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    # Retrieve the instance ID from the event
    instance_id = event['detail']['instance-id']

    tags = [
        {
            'Key': 'LaunchDate',
            'Value': datetime.now().strftime('%Y-%m-%d')
        },
        {
            'Key': 'YourCustomTag',
            'Value': 'YourValue'
        }
    ]

    # Tag the new instance
    ec2.create_tags(Resources=[instance_id], Tags=tags)

    logger.info(f"Instance {instance_id} has been tagged with: {tags}")

if __name__ == "__main__":
    lambda_handler(None, None)
