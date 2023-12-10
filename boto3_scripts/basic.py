import boto3
import csv

session = boto3.Session()
s3 = session.client('s3')

buckets = s3.list_buckets()

with open('s3_buckets_and_objects.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Bucket Name', 'Object Name'])

    for bucket in buckets['Buckets']:
        bucket_name = bucket['Name']
        print(f"Processing bucket: {bucket_name}")

        try:
            objects = s3.list_objects_v2(Bucket=bucket_name)
            if 'Contents' in objects:
                for obj in objects['Contents']:
                    writer.writerow([bucket_name, obj['Key']])
        except Exception as e:
            print(f"Error processing bucket {bucket_name}: {e}")

print("S3 buckets and objects have been saved to s3_buckets_and_objects.csv")