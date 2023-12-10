import boto3
import csv

class EC2Manager:
    def __init__(self, image_id, instance_type, key_name, bucket_name):
        self.ec2 = boto3.resource('ec2')
        self.s3 = boto3.client('s3')
        self.image_id = image_id
        self.instance_type = instance_type
        self.key_name = key_name
        self.bucket_name = bucket_name
        self.instance = None

    def create_instance(self):
        self.instance = self.ec2.create_instances(
            ImageId=self.image_id,
            MinCount=1,
            MaxCount=1,
            InstanceType=self.instance_type,
            KeyName=self.key_name
        )[0]
        self.instance.wait_until_running()
        self.instance.load()
        print(f"Instance created with ID: {self.instance.id}")
        return self.instance.id

    def stop_instance(self):
        self.instance.stop()
        self.instance.wait_until_stopped()
        print(f"Instance {self.instance.id} stopped.")

    def delete_instance(self):
        self.instance.terminate()
        self.instance.wait_until_terminated()
        print(f"Instance {self.instance.id} terminated.")

    def save_instance_state_to_csv(self, csv_file_name):
        with open(csv_file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Instance ID', 'State'])
            writer.writerow([self.instance.id, self.instance.state['Name']])
        print(f"Instance state saved to {csv_file_name}")

    def upload_csv_to_s3(self, csv_file_name):
        self.s3.upload_file(csv_file_name, self.bucket_name, csv_file_name)
        print(f"CSV file uploaded to S3 bucket {self.bucket_name}")

image_id = 'ami-0e83be366243f524a'  
instance_type = 't2.micro'         
key_name = 'zclapaws01'         
bucket_name = 'zclap-public'    

manager = EC2Manager(image_id, instance_type, key_name, bucket_name)
instance_id = manager.create_instance()
csv_file_name = 'ec2_instance_state.csv'
manager.save_instance_state_to_csv(csv_file_name)
manager.upload_csv_to_s3(csv_file_name)
manager.stop_instance()
manager.delete_instance()
