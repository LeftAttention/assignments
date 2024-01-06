import boto3
import logging
from datetime import datetime, timedelta

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def lambda_handler(event, context):
    cloudwatch = boto3.client('cloudwatch')
    sns = boto3.client('sns')

    sns_topic_arn = 'arn:aws:sns:us-east-2:160472638876:BillingAlerts'
    billing_threshold = 50.0

    # Retrieve the AWS billing metric from CloudWatch
    response = cloudwatch.get_metric_data(
        MetricDataQueries=[
            {
                'Id': 'billing',
                'MetricStat': {
                    'Metric': {
                        'Namespace': 'AWS/Billing',
                        'MetricName': 'EstimatedCharges',
                        'Dimensions': [{'Name': 'Currency', 'Value': 'USD'}]
                    },
                    'Period': 86400,
                    'Stat': 'Maximum',
                },
                'ReturnData': True,
            },
        ],
        StartTime=datetime.now() - timedelta(days=1),
        EndTime=datetime.now()
    )

    # Check if billing exceeds the threshold
    if response['MetricDataResults'][0]['Values']:
        current_billing = response['MetricDataResults'][0]['Values'][0]
        if current_billing > billing_threshold:
            # Send an SNS notification
            sns.publish(
                TopicArn=sns_topic_arn,
                Message=f'Alert: Your AWS billing has exceeded ${billing_threshold}. Current billing: ${current_billing}',
                Subject='AWS Billing Alert'
            )
            logger.info("SNS alert sent.")

    logger.info("Billing check completed.")

if __name__ == "__main__":
    lambda_handler(None, None)
