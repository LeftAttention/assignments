import boto3
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    instances_to_stop = ec2.describe_instances(Filters=[
        {'Name': 'tag:Auto-Stop', 'Values': ['true']}
    ])

    instances_to_start = ec2.describe_instances(Filters=[
        {'Name': 'tag:Auto-Start', 'Values': ['true']}
    ])

    stop_ids = [instance['InstanceId'] for reservation in instances_to_stop['Reservations'] for instance in reservation['Instances']]
    start_ids = [instance['InstanceId'] for reservation in instances_to_start['Reservations'] for instance in reservation['Instances']]

    # Stop instances
    if stop_ids:
        ec2.stop_instances(InstanceIds=stop_ids)
        logger.info(f'Stopped instances: {stop_ids}')

    # Start instances
    if start_ids:
        ec2.start_instances(InstanceIds=start_ids)
        logger.info(f'Started instances: {start_ids}')

    return {
        'StoppedInstances': stop_ids,
        'StartedInstances': start_ids
    }

