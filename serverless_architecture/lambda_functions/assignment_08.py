import boto3
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def lambda_handler(event, context):
    sns = boto3.client('sns')
    sns_topic_arn = 'arn:aws:sns:us-east-2:160472638876:DynamoDB'

    for record in event['Records']:
        # Check for MODIFY event type
        if record['eventName'] == 'MODIFY':
            # Extract new and old images
            new_image = record['dynamodb'].get('NewImage', {})
            old_image = record['dynamodb'].get('OldImage', {})

            message = {
                'Message': 'DynamoDB record modified',
                'NewImage': new_image,
                'OldImage': old_image
            }

            # Send an SNS notification
            sns.publish(
                TopicArn=sns_topic_arn,
                Message=json.dumps(message),
                Subject='DynamoDB Update Notification'
            )

            logger.info("SNS notification sent for modified record.")
