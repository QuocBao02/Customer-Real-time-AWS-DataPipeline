---
title : "Real-time Customers Data Pipeline with AWS Services"
date :  "`r Sys.Date()`" 
weight : 0
chapter : false
---
# Work with Amazon Processing - Storage - Visualization Services 

### Overall
This project aims to build a real-time data pipeline for customer data on an e-commerce platform using AWS services. This will allow the owner to gain clear insights into customer demographics(age, gender, locations, etc.), product consumption patterns, best-selling products, and more. With this information, the owner can make informed decisions to benefit the company.

* Data Ingestion: **AWS Kinesis**
* Processing data : **AWS Lambda**
* Storange data( Data Lake): **AWS S3**
* Database(Data Warehouse): **AWS Redshift**
* Analystic (Visualization): **Redshift visualization tool** 


![Infrastructure](/images/Overview/overview.jpg) 

### Table of Contents
1. [Introduction ](1-introduce/)
2. [Kinesis Data Ingesion](2-kinesis/)
3. [Lambda Data Processing](3-lambda/)
4. [Running Data Pipeline and Visualization Redshift Data](4-redshiftvisualize/)
5. [Clean up resources](5-cleanup/)
