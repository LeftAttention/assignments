import boto3
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def lambda_handler(event, context):
    rds_instance_identifier = 'leftattention-rds02-identifier'
    rds = boto3.client('rds')

    # Generate a snapshot identifier
    snapshot_identifier = f"{rds_instance_identifier}-snapshot-{datetime.now().strftime('%Y-%m-%d')}"

    # Take a snapshot of the specified RDS instance
    response = rds.create_db_snapshot(DBSnapshotIdentifier=snapshot_identifier, DBInstanceIdentifier=rds_instance_identifier)

    snapshot_id = response['DBSnapshot']['DBSnapshotIdentifier']
    logger.info(f'Created snapshot: {snapshot_id}')

    return {
        'SnapshotID': snapshot_id
    }

