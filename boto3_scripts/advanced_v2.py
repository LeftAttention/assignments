import boto3
import os
import time
from PIL import Image
from io import BytesIO
import logging

class S3ImageOptimizer:
    def __init__(self, bucket_name, upload_folder='upload/', optimized_folder='optimized/', polling_interval=50):
        self.s3 = boto3.client('s3')
        self.bucket_name = bucket_name
        self.upload_folder = upload_folder
        self.optimized_folder = optimized_folder
        self.polling_interval = polling_interval
        self.processed_images = set()
        self.setup_logger()

    def setup_logger(self):
        self.logger = logging.getLogger('S3ImageOptimizer')
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def is_image(self, filename):
        return filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'))

    def compress_image(self, image):
        img = Image.open(image)
        img_io = BytesIO()
        img.save(img_io, format='JPEG', quality=70)
        img_io.seek(0)
        return img_io

    def process_new_images(self):
        response = self.s3.list_objects_v2(Bucket=self.bucket_name, Prefix=self.upload_folder)
        if 'Contents' in response:
            for item in response['Contents']:
                file_name = item['Key']
                if self.is_image(file_name) and file_name not in self.processed_images:
                    self.logger.info(f"Processing new image: {file_name}")
                    self.s3.download_file(self.bucket_name, file_name, '/tmp/' + os.path.basename(file_name))
                    with open('/tmp/' + os.path.basename(file_name), 'rb') as file:
                        optimized_image = self.compress_image(file)
                    self.s3.upload_fileobj(optimized_image, self.bucket_name, self.optimized_folder + os.path.basename(file_name))
                    self.processed_images.add(file_name)

    def start_monitoring(self):
        self.logger.info("Starting to monitor the bucket for new images...")
        while True:
            self.process_new_images()
            time.sleep(self.polling_interval)

bucket_name = 'zclap-public'  
optimizer = S3ImageOptimizer(bucket_name)
optimizer.start_monitoring()
