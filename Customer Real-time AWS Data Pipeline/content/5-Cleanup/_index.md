---
title : "Clean up resources"
date :  "`r Sys.Date()`" 
weight : 0
chapter : false
pre : " <b> 5. </b> "
---

* We will take the following steps to delete the resources we created in this project.

#### Delete Redshift Workgroup and Namespace

1. Go to [Redshift service management console](https://us-east-1.console.aws.amazon.com/redshiftv2/home)
   + Select **Workgroup configuration**.
   + From the **Actions** menu, select **Delete workgroup**.
   ![image](/images/Clean/Redshift/1.png) 
   + Enter **delete**, then click **Delete** to proceed to delete workgroup.
   ![image](/images/Clean/Redshift/2.png)
   + Select **Namespace configuration**.
   + From the **Actions** menu, select **Delete namespace**.
   ![image](/images/Clean/Redshift/3.png) 
   + Enter **delete**, then click **Delete** to proceed to delete namespace.
   ![image](/images/Clean/Redshift/4.png)

#### Delete S3 bucket

1. Go to [S3 service management console](https://s3.console.aws.amazon.com/s3/home)
   + Click on the S3 bucket we created for this project: **customer-data-datalake-quocbao**
   + Click **Empty**.
   ![image](/images/Clean/S3/1.png)
   + Enter **permanently delete**, then click **Empty** to proceed to delete the object in the bucket.
   ![image](/images/Clean/S3/2.png)
   + Click **Exit**.

2. After deleting all objects in the bucket, click **Delete**

![image](/images/Clean/S3/3.png)

3. Enter the name of the S3 bucket, then click **Delete bucket** to proceed with deleting the S3 bucket.

![image](/images/Clean/S3/4.png)


#### Delete Lamdba function
1. Go to [Lambda service management console](https://us-east-1.console.aws.amazon.com/lambda/home)
   + Click 2 lambda functions we created for this project: **kinesis-event-processor-to-s3** and **etl-s3-to-redshift**
   + From the **Actions** menu, select **Delete**.
   ![image](/images/Clean/Lambda/1.png)
   + Enter **delete**, then click **Delete** to proceed to delete lambda functions.
   ![iamge](/images/Clean/Lambda/2.png)

#### Delete Kinesis data stream
1. Go to [Kinesis service management console](https://us-east-1.console.aws.amazon.com/kinesis/home)
   + Click Kinesis data stream we created for this project: **CustomersDataStream**
   + From the **Actions** menu, select **Delete**.
   ![image](/images/Clean/Kinesis/1.png)
   + Enter **delete**, then click **Delete** to proceed to delete kinesis data stream
   ![iamge](/images/Clean/Kinesis/2.png)

#### Delete VPC

1. Go to [VPC service management console](https://console.aws.amazon.com/vpc/home)
   + Click **Your VPCs**, select **default VPC** we created for this project.
   + From the **Actions** menu, select **Delete VPC**.
   ![image](/images/Clean/VPC/1.png)

2. In the confirm box, enter **delete default vpc** to confirm, click **Delete** to delete **VPC** and related resources.
![iamge](/images/Clean/VPC/2.png)