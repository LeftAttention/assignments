import boto3
import logging
from datetime import datetime, timezone, timedelta

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def lambda_handler(event, context):
    volume_id = 'vol-060a8de8c2b73a676'
    ec2 = boto3.client('ec2')

    snapshot = ec2.create_snapshot(VolumeId=volume_id, Description='Automated backup')
    logger.info(f'Created snapshot: {snapshot["SnapshotId"]}')

    current_time = datetime.now(timezone.utc)

    # List snapshots for the specified volume
    snapshots = ec2.describe_snapshots(OwnerIds=['self'], Filters=[{'Name': 'volume-id', 'Values': [volume_id]}])

    # Delete snapshots older than 30 days
    for snap in snapshots['Snapshots']:
        creation_time = snap['StartTime']
        age_in_days = (current_time - creation_time).days
        if age_in_days > 30:
            ec2.delete_snapshot(SnapshotId=snap['SnapshotId'])
            logger.info(f'Deleted snapshot: {snap["SnapshotId"]}')
