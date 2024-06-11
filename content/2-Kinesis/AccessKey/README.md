---
title : "Create AWS Access Key"
date :  "`r Sys.Date()`" 
weight : 1 
chapter : false
pre : " <b> 1. </b> "
---

### Create AWS Access Key
* In this project, we will interact with AWS using the CLI (Command Line Interface). Therefore, we need to create an Access Key to enable this connection.

### Step-by-Step Guide:
1. Sign in to AWS Management Console and go to search box "**IAM**"
![iam](/images/Kinesis/1.png)
2. Select **Manage access keys** to create new key
![manage access key](/images/Kinesis/2.png)
3. Select **Create access key**
![access key](/images/Kinesis/3.png)
4. For this project, I will grant root permission for this key. Additionally, you can create an IAM user for specific purposes. Click **Create Access key** to proceed.
![root](/images/Kinesis/4.png)
5. Once the Access Keys is created, be sure to note it down and keep it confidential. For more convenience, you can download the access key information as a CSV file.
![done](/images/Kinesis/5.png)
6. Well done!




