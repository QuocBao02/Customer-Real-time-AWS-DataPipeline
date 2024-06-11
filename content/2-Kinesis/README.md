---
title : "Kinesis Data Ingestion"
date :  "`r Sys.Date()`" 
weight : 1 
chapter : false
pre : " <b> 2. </b> "
---

* In this section, I will create an AWS Access Key to connect my local data generator and send data to Kinesis using boto3 Python library

## Overview of Boto3
*  **Boto3** is the Amazon Web Services (AWS) SDK for Python, which allows Python developers to write software that makes use of services like Amazon S3 and Amazon EC2.
* In this project, **boto3** is used to interact with Amazon Kinesis, enabling the sending of real-time data to the Kinesis stream  programmatically.
## Amazon Kinesis  Data Stream
* **Amazon Kinesis** is a platform on AWS to collect, process, and analyze real-time, streaming data.

* Kinesis allows me to ingest customer data in real time from various sources such as web applications, mobile apps, or IoT devices. In this project, I used local data generator for data source.


## Contents
1. [Create AWS Access Key](AccessKey)
2. [Generate Customer Data](GenerateData)
3. [Create Kinesis Stream Key](KinesisStreamKey)