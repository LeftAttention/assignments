# Lambda Functions


assignment_01.py

## [1. Automated Instance Management Using AWS Lambda and Boto3](assignment_01.py)

**Objective**: Automate the stopping and starting of EC2 instances based on `Auto-Stop` and `Auto-Start` tags.

**Script Functionality**:
1. **Initialize Boto3 EC2 Client**: Establishes a connection with AWS EC2 service.
2. **Describe Instances**: Retrieves instances that have either `Auto-Stop` or `Auto-Start` tags.
3. **Stop and Start Instances**: Stops instances with `Auto-Stop` tag and starts instances with `Auto-Start` tag.


## [2. Automated S3 Bucket Cleanup Using AWS Lambda and Boto3](assignment_02.py)

**Objective**: Automate the deletion of files older than 30 days in a specific S3 bucket.

**Script Functionality**:
1. **Initialize Boto3 S3 Client**: Establishes a connection with AWS S3 service.
2. **List Objects**: Retrieves all objects in the specified S3 bucket.
3. **Delete Old Objects**: Deletes objects that are older than 30 days from the current date.