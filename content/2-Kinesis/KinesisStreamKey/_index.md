---
title : "Create Kinesis Stream Key"
date :  "`r Sys.Date()`" 
weight : 3
chapter : false
pre : " <b> 3. </b> "
---
### Create Kinesis Stream Key
1. Return to your AWS account and type **Kinesis** in the search box to create a stream.
![image](/images/Kinesis/10.png)
2. Select **Kinesis Data Stream** and click **Create data stream**
![image](/images/Kinesis/11.png)
3. Stream key name is : `CustomersDataStream`, Select **Provisioned** data stream capacity and **Provisioned shards** is **1**. Click **Create data stream**. 
![image](/images/Kinesis/12.png)
4. **CustomersDataStream** is created and actived.
![image](/images/Kinesis/13.png)
5. Run the Data Generator by executing the `python fakedata.py` file and then view the results.
![image](/images/Kinesis/14.png)
6. Let's open the Amazon Kines console and check if the  **CustomersDataStream** you created previously exists.  In Data Viewer, select the shard **shardid-00000000000**, and set **Starting posistion** to **Trim horizon**. Click **Get records** to view the incoming data.
![image](/images/Kinesis/15.png)
