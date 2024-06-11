---
title : "Lambda Data Processing"
date :  "`r Sys.Date()`" 
weight : 1 
chapter : false
pre : " <b> 3. </b> "
---


* In this section, I will define two Lambda functions. The first retrieves the latest data data from Kinesis and saves it to an S3 bucket for the data lake. The second function then extracts, transforms, and loads the newly added objects in the S3 bucket to Redshift, a relational database for the data warehouse.
## Lambda
* AWS lambda is a cloud service designed to execute code in response to specific events and automatically manages the underlying compute resources. We simply upload your code in the form of a Lambda function, and the service takes care of everything required to run and scale the code with high availability.
![image](/images/Lambda/lambda_overview.png)
## Contents 
1. [Get Data From Kinesis to S3](./lambda-to-s3/)
3. [ETL Data From S3 to Redshift](./lambda-to-redshift/)