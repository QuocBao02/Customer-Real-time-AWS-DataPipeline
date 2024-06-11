---
title : "Introduction"
date :  "`r Sys.Date()`" 
weight : 1 
chapter : false
pre : " <b> 1. </b> "
---
This project aims to build a real-time data pipeline for customer data on an e-commerce platform using AWS services. This will allow the owner to gain clear insights into customer demographics(age, gender, locations, etc.), product consumption patterns, best-selling products, and more. With this information, the owner can make informed decisions to benefit the company.

![Overview](/images/Overview/overview.jpg)

## System Infrastructure

* Data source: Data will be crawled from customers who made the transactions. In this case, i will use the **Fake** Python library to generate customer data.
* Data Ingestion: **AWS Kinesis**, after data is generated, it will be sent to AWS Kinesis using the **boto3** Python library and an **AWS Access Point**
* Processing data : **AWS Lambda** will be trigged by **AWS Kinesis** when new data arrives. Lambda acts as a transformer, moving data from **AWS Kinesis** to **AWS S3**
* Storange data( Data Lake): **AWS S3** will save the raw data, acting as a Data Lake to maintain data purity.
* Database(Data Warehouse): **AWS Redshift** serves as the data warehouse, containing relational customer data. A Lambda function will be trigged to perform ELT tasks when new data arrives in S3.
* Analystic (Visualization): **AWS QuickSight** provides an overview of customer activities and product sales to the Owner. **QuickSight** will create dashboard to help the Owner make informed the decisions to benefit the company.


## Data Source Overview

The format of customer data looks like:

```
Data Description: Customer Data
        Example: 
            Name: 'Laura Salazar'
            Address: '98201 Moore Cliffs Apt. 537 Jamesburgh, NV 21021'
            Phone: '763-957-9359x022'
            Age: 20
            Gender: M or F
            Product Name: 'Canon EOS R5'
            Amount: 100
            Purchase Date: '2010-01-11'
```