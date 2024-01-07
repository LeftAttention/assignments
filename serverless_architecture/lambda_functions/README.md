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

### Setting Up CloudWatch Event Rule:


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



## [4.Monitor Unencrypted S3 Buckets Using AWS Lambda and Boto3](assignment_04.py)

**Objective**: Automate the detection of S3 buckets that don't have server-side encryption enabled.

**Script Functionality**:
1. **Initialize Boto3 S3 Client**: Establishes a connection with AWS S3 service.
2. **List All S3 Buckets**: Retrieves a list of all S3 buckets in our AWS account.
3. **Detect Unencrypted Buckets**: Checks each bucket for server-side encryption configuration.


## [5. Automatic EBS Snapshot and Cleanup Using AWS Lambda and Boto3](assignment_05.py)

**Objective**: Automate the creation of snapshots for specified EBS volumes and clean up snapshots older than 30 days.

**Script Functionality**:
1. **Initialize Boto3 EC2 Client**: Establishes a connection with AWS EC2 service.
2. **Create Snapshot**: Generates a snapshot of the specified EBS volume.
3. **List and Delete Old Snapshots**: Identifies and deletes snapshots older than 30 days.

### Setting Up CloudWatch Event Rule:

#### Step 1: Creating a New Rule

1. **Open the Rules Page**: In the CloudWatch dashboard, click on "Rules" under the "Events" section in the left sidebar.

2. **Create a New Rule**: Click on the “Create rule” button, usually located at the top right of the page.

#### Step 2: Configuring the Event Source

1. **Select Event Source**: Under the "Event Source" section, choose "Schedule". We can choose between a fixed rate or a cron expression.
   - **Fixed Rate**: Allows us to set a simple frequency, like every 7 days.
   - **Cron Expression**: For more complex schedules. For a weekly trigger, we might use an expression like `0 0 * * SUN`, which triggers the function every Sunday at midnight UTC.

2. **Enter the Schedule Details**: Based on our choice, input the fixed rate or cron expression.

#### Step 3: Setting the Target

1. **Choose Target**: Under the "Targets" section, click "Add target". Then select “Lambda function” as the target type.

2. **Select Our Lambda Function**: From the drop-down, choose the Lambda function we created for the EBS snapshot and cleanup.

3. **Configure Additional Settings**: If needed, configure additional settings like input constants or a dead-letter queue for handling failures.

#### Step 4: Configuring the Rule

1. **Name the Rule**: Provide a descriptive name for our rule. This helps in identifying the rule in the future.

2. **Add a Description**: Optionally, we can add a description for more clarity on the rule’s purpose.

3. **Set IAM Role**: AWS may prompt us to assign an IAM role that grants CloudWatch Events permission to invoke our Lambda function. We can choose an existing role or create a new one.

4. **Enable the Rule**: Ensure that the state of the rule is set to "Enabled" to make it active immediately upon creation.

#### Step 5: Review and Create

1. **Review Our Configuration**: Double-check all the settings to ensure they match our intended schedule and target.

2. **Create the Rule**: Click on the “Create” button to finalize the creation of the event rule.


## [6. Auto-Tagging EC2 Instances](assignment_06.py)

### Setting Up CloudWatch Event Rule

1. Navigate to the **CloudWatch** service.

2. In the CloudWatch dashboard, go to the **Rules** page under **Events**.

3. **Create a new rule**:
   - For **Event Source**, select **Event Pattern**.
   - Choose **EC2** as the service and **EC2 Instance State-change Notification** as the event type.
   - Select **specific state(s)** and choose **running**. This triggers the function when instances are launched and reach the running state.

4. In the **Targets** section, add your Lambda function.

5. **Configure the details** of the rule:
   - Provide a **name** and **description** for the rule.
   - Ensure the rule is set to **Enabled**.

6. **Review and create** the rule.

## [7. Monitor and Alert High AWS Billing Using AWS Lambda, Boto3, and SNS](assignment_07.py)

### Step 1: SNS Setup

1. Navigate to the **Simple Notification Service (SNS)** dashboard.

2. **Create a New Topic**:
   - Click on “Create topic”.
   - Give it a name and a display name (e.g., `BillingAlerts`).
   - Click “Create”.

3. **Subscribe to the Topic**:
   - Select the topic you just created.
   - Click on “Create subscription”.
   - Select “Email” as the protocol and enter your email address.
   - Click “Create subscription”.
   - You will receive an email to confirm the subscription. Make sure to confirm it.


### Step 2: Event Source Setup

1. **Navigate to CloudWatch**: Go to the CloudWatch service.

2. **Create a New Rule**:
   - Go to “Rules” under “Events”.
   - Click “Create rule”.
   - Choose “Schedule”.
   - Set a fixed rate of 1 day or use a cron expression for daily execution.

3. **Set Lambda as the Target**:
   - In the “Targets” section, choose the Lambda function you created for this task.

4. **Configure and Enable the Rule**:
   - Provide a name and description.
   - Ensure the rule is enabled.
   - Click “Create”.


## [8. DynamoDB Item Change Alert Using AWS Lambda, Boto3, and SNS](assignment_08.py)

### Setting Up the DynamoDB Stream and Lambda Trigger

1. **Enable DynamoDB Streams on Your Table**:
   - Go to the DynamoDB console, select your table, and go to the “Streams” tab.
   - Enable stream and select “New and old images” as the view type. This allows the Lambda function to see both the previous and updated state of the item.

2. **Set up the Lambda Trigger**:
   - In the Lambda function’s configuration, add a trigger.
   - Select DynamoDB as the source and choose the table you enabled the stream on.
   - Ensure the event source is enabled.

## [9 Analyze Sentiment of User Reviews Using AWS Lambda, Boto3, and Amazon Comprehend](assignment_09.py)

**EventBridge Setup**:
- **Event Source**: Configure an event source that triggers the Lambda function. This could be based on a schedule or another AWS service event.
- **Event Pattern**: If triggering based on a specific event, define an event pattern that includes the `user_review` data. For example, if the review is part of an S3 event or a custom application event, ensure the `user_review` field is included in the event pattern.
- **Test Event**: For testing, you can create a sample event in the AWS Lambda console with a JSON structure like `{'user_review': 'Sample review text'}`.

## [10: Archive Old Files from S3 to Glacier Using AWS Lambda and Boto3](assignment_10.py)

### Objective
Automate the archival of files older than 6 months from an S3 bucket to Amazon Glacier for cost-effective long-term storage.

### Setup and Deployment

1. **Trigger**:
   - Configure the Lambda function to run periodically (e.g., daily or weekly) using AWS EventBridge (formerly CloudWatch Events).

## [11. Notify When ELB 5xx Errors Spike Using AWS Lambda, Boto3, and SNS](assignment_11.py)


### Objective
Automatically receive notifications when your Elastic Load Balancer (ELB) encounters an unusually high number of 5xx errors.

### Setup and Deployment

1. **Lambda Function**:

2. **SNS Topic Setup**:
   - Create an SNS topic and subscribe to it with your preferred method (e.g., email, SMS).
   - Note the ARN of the SNS topic and use it in the script.

3. **ELB Configuration**

4. **Trigger**:
   - Schedule the Lambda function to run every 5 minutes using AWS EventBridge.