import boto3
import logging
from datetime import datetime, timedelta

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def lambda_handler(event, context):
    # CloudWatch and SNS clients initialization
    cloudwatch = boto3.client('cloudwatch')
    sns = boto3.client('sns')

    # ELB and SNS configuration
    elb_name = 'leftattention-elb'
    sns_topic_arn = 'arn:aws:sns:us-east-2:160472638876:Error'
    error_threshold = 10  # Threshold for 5xx errors

    # Fetch ELB 5xx error count from CloudWatch
    response = cloudwatch.get_metric_statistics(
        Namespace='AWS/ELB',
        MetricName='HTTPCode_ELB_5XX_Count',
        Dimensions=[{'Name': 'LoadBalancerName', 'Value': elb_name}],
        StartTime=datetime.utcnow() - timedelta(minutes=5),
        EndTime=datetime.utcnow(),
        Period=300,
        Statistics=['Sum']
    )

    # Check if error count exceeds threshold
    if response['Datapoints']:
        error_count = response['Datapoints'][0]['Sum']
        if error_count > error_threshold:
            # Trigger an SNS notification
            message = f"High 5xx error count detected in ELB '{elb_name}'. Error count in the last 5 minutes: {error_count}"
            sns.publish(TopicArn=sns_topic_arn, Message=message, Subject="ELB 5xx Error Alert")
            logger.info("SNS notification sent.")

    logger.info("ELB 5xx error check completed.")