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


## [3. Automated RDS Snapshot Using AWS Lambda and Boto3](assignment_03.py)

**Objective**: Automate the creation of a snapshot for a specific RDS instance at regular intervals.

**Script Functionality**:
1. **Initialize Boto3 RDS Client**: Establishes a connection with AWS RDS service.
2. **Take Snapshot**: Creates a snapshot of the specified RDS instance.

**Setting Up CloudWatch Event Rule**:


#### Step 1: Creating a New Rule

1. **Open the Rules Page**: In the CloudWatch dashboard, select "Rules" under the "Events" section on the left-hand menu.

2. **Click on 'Create Rule'**: We'll find a button usually at the top right corner to create a new rule.

#### Step 2: Configuring the Event Source

1. **Select Event Source**: Under the "Event Source" section, choose "Schedule". We have two options: a fixed rate or a cron expression.
   - **Fixed Rate**: Allows us to select a pre-defined interval (e.g., every 5 minutes, every day).
   - **Cron Expression**: For more specific schedules. For a daily trigger, we might use a cron expression like `0 12 * * ? *`, which means the function will be triggered every day at 12:00 PM UTC.

2. **Enter the Schedule**: Depending on our choice, enter the rate or the cron expression.

#### Step 3: Setting the Target

1. **Choose Target**: Under the "Targets" section, click on "Add target" and then select "Lambda function".

2. **Select Our Lambda Function**: In the drop-down list, choose the Lambda function we have created for the RDS snapshot.

3. **Configure Additional Settings if Necessary**: Depending on our requirements, we can add additional configurations like input constants or configure a dead-letter queue.

#### Step 4: Configuring the Rule

1. **Name the Rule**: Provide a meaningful name for the rule, which will help us to identify it later.

2. **Add a Description (Optional)**: While optional, it's a good practice to add a description for clarity.

3. **Set Permissions**: AWS might prompt us to assign a role or create a new role. This IAM role should have permissions to invoke our Lambda function.

4. **Enable the Rule**: Make sure the "State" is set to "Enabled" to ensure the rule is active.

#### Step 5: Review and Create

1. **Review the Settings**: Make sure all configurations are correct as per our requirements.

2. **Create the Rule**: Click on the "Create" button to create the event rule.

Once this rule is created, it will automatically trigger our AWS Lambda function at the specified intervals, executing the task of creating an RDS snapshot.

