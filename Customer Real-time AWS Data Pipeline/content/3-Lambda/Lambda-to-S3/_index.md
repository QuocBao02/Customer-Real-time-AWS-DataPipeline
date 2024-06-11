---
title : "Load Data From Kinesis to S3"
date :  "`r Sys.Date()`" 
weight : 1 
chapter : false
pre : " <b> 1. </b> "
---

* In this section, I will walk you through the steps involved in setting up the data pipeline: Creating an S3 bucket for the data lake, an IAM role for the Lambda function to access S3 and other project services, a Lambda function to move data from Kinesis to S3, and a trigger for this Lambda function. Let's dive into the details below.

## Amazon Simple Storage Service - S3 
* Amazon S3 is an object storage service that provides high scalability, data availability, security, and performance. It's one of the core services offered by AWS and is used by millions of customers to store and manage data for various use cases:

## Step-by-Step Guide:
### Create Lambda Role
1. Go to [IAM service management console](https://us-east-1.console.aws.amazon.com/iam/home)
    + Select **Create role** to create new role for Lambda function.
    ![image](/images/Lambda/Lambda-to-S3/1.png)
    + Select **Lambda** for **AWS service**, then click **Next**.
    ![image](/images/Lambda/Lambda-to-S3/2.png)
    + Add **CloudwatchFullAccess** to **Permission policies**.
    ![image](/images/Lambda/Lambda-to-S3/3.png)
    + Add **AmazonS3FullAccess** to **Permission policies**.
    ![image](/images/Lambda/Lambda-to-S3/4.png)
    + Add **AmazonKinesisFullAccess** to **Permission policies**.
    ![image](/images/Lambda/Lambda-to-S3/5.png)
    + Add **AmazonRedshiftFullAccess** to **Permission policies**.
    ![image](/images/Lambda/Lambda-to-S3/6.png)
    + Set **Role name** is **full-customer-data-stream-role** and click **Create role**.
    ![image](/images/Lambda/Lambda-to-S3/7.png)
    ![image](/images/Lambda/Lambda-to-S3/8.png)

### Create S3 bucket for the data lake
1. Go to [S3 service management console](https://s3.console.aws.amazon.com/s3/home) 
    + Select **Create bucket** to create new bucket.
    + Set **Bucket name** is **customer-data-datalake-quocbao**, It must be unique within the global namespace and follow the bucket naming rules. Then, Click **Create bucket**.
    ![image](/images/Lambda/Lambda-to-S3/16.png)
    ![image](/images/Lambda/Lambda-to-S3/17.png)
    + Well done!, S3 bucket is created!
    ![image](/images/Lambda/Lambda-to-S3/18.png)

### Create Lambda function to move data from Kinesis to S3
1. Go to [Lambda service management console](https://us-east-1.console.aws.amazon.com/lambda/home)
    + Select **Create a function** to create new lambda function.
    ![image](/images/Lambda/Lambda-to-S3/10.png)
    + Set **Function name** is **kinesis_event_processor_to_s3**, **Runtime type** is **Python 3.12**, **Architecture** is **x86_64**. Select **Use an existing role** to set my lambda role was create before. Then click **Create function**.
    ![image](/images/Lambda/Lambda-to-S3/11.png)
2. Add lambda function code.
    + Select **Code** and paste the code source below before clicking **Deploy**.
    ```python
        import json
        import boto3
        import time

        def generate_partition():
            '''Create directory to save data into data lake in hadoop hdfs'''
            current_time=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            date_string = current_time.split()[0].split('-')
            time_string = current_time.split()[1].split(':')
            year=date_string[0]
            month=date_string[1]
            day=date_string[2]
            hour=time_string[0]
            minute=time_string[1]
            second=time_string[2]
            
            prefix = "data-" + day + "-" + month + "-" + year + "/"
            data="event-"+hour+"-"+minute+"-"+second+".json"
            return prefix+data


        s3_cli = boto3.client("s3")
        bucket_name = "customer-data-datalake-quocbao"

        def lambda_handler(event, context):
            object_name = generate_partition()
            # print(event)
            # print(object_name)
            s3_cli.put_object(
                    Bucket=bucket_name,
                    Key=object_name,
                    Body=json.dumps(event).encode("utf-8")
            )
            return {
                'statusCode': 200
            }
    ```
    ![image](/images/Lambda/Lambda-to-S3/12.png)
3. Add trigger to Lambda function
![image](/images/Lambda/Lambda-to-S3/13.png)
    + Select **Add trigger** and choose **Kinesis** source.
    ![image](/images/Lambda/Lambda-to-S3/14.png)
    + Set **Kinesis stream** is **kinesis/CustomersDataStream**, the kinesis stream key was created before. **Batch size** is 1. Click **Add** to finish add trigger for **kinesis_event_processor_to_s3**
    ![image](/images/Lambda/Lambda-to-S3/15.png)
