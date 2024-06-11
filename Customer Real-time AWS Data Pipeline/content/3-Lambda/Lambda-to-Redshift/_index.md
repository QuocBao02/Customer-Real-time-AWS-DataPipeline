---
title : "ELT Data From S3 to Redshift"
date :  "`r Sys.Date()`" 
weight : 2 
chapter : false
pre : " <b> 2. </b> "
---
* In this section, I will create a lambda function to load the newly added objects in the S3 bucket to Redshift. Moreover, I will also create Redshift cluster, VPC, S3 endpoint and design data model for redshift relational database.

## Amazon Redshift 
* AWS Redshift is a cloud-based data warehouse service. It's designed to handle massive datasets, scaling up to petabytes in size.

* Data source: 
```
Data Description: Fake Customer Data
        Example: 
            Customer ID: 1
            Name: 'Laura Salazar'
            Address: '98201 Moore Cliffs Apt. 537 Jamesburgh, NV 21021'
            Phone: '763-957-9359x022'
            Age: 20
            Gender: M or F
            Product ID: 1
            Product Name: 'Canon EOS R5'
            Price: 1000
            Amount: 100
            Transaction ID: 1
            Purchase Date: '2010-01-11'
```
* Data Model:
![image](/images/Lambda/Lambda-to-Redshift/datamodel.png)
    + **customers** table: the primary key is **id**
    + **products** table: the primary key is **product_ID**
    + **transactions** table:
        + The primary key is **transaction_id**
        + The foreign key **customer_ID** references the **id** column in the **customers** table.
        + The foreign key **product_ID** references the **product_ID** column in the **products** table.
## Step-by-Step Guide:
### Create default Virtual Private Cloud (VPC) and S3 Endpoint
#### Create default VPC.
1. Go to [VPC service management console](https://console.aws.amazon.com/vpc/home)
    ![image](/images/Lambda/Lambda-to-Redshift/1.png)
   + Click **Your VPCs**, from the **Actions** menu, select **Create default VPC** to create default VPC.
   ![image](/images/Lambda/Lambda-to-Redshift/2.png)
   ![image](/images/Lambda/Lambda-to-Redshift/3.png)
    + Well done!
    ![image](/images/Lambda/Lambda-to-Redshift/4.png)
#### Create S3 Endpoint
* In the left sidebar, select **Endpoint**, then click **Create Endpoint**
![image](/images/Lambda/Lambda-to-Redshift/5.png)
* Set **Name tag** is **s3-endpoint-quocbao**, **Service** select **s3 gateway**, and click **Create Endpoint**
![image](/images/Lambda/Lambda-to-Redshift/6.png)
![image](/images/Lambda/Lambda-to-Redshift/7.png)
### Create Redshift for the data warehouse
1. Go to [Redshift service management console](https://us-east-1.console.aws.amazon.com/redshiftv2/home)
    ![image](/images/Lambda/Lambda-to-Redshift/8.png)
    + Create Redshift serverless. Set **namespace** is **quocbao-namespace**. Customize admin user credentials: **Admin user name** is **admin**, **Admin user password** is **Password123**
    ![image](/images/Lambda/Lambda-to-Redshift/9.png)
    + Set **workgroup** is **quocbao-workgroup**, select **default VPC and subnets**created before.
    ![image](/images/Lambda/Lambda-to-Redshift/10.png)
    + Wait a minute for creating Redshift cluster
    ![image](/images/Lambda/Lambda-to-Redshift/11.png)
    ![image](/images/Lambda/Lambda-to-Redshift/12.png)
    + Create Redshift endpoint
    ![image](/images/Lambda/Lambda-to-Redshift/13.png)
### Create Lambda function to load the newly added objects in the S3 bucket to Redshift.
1. Create another lambda function named: **etl_s3_to_redshift**
    + Set **Function name** is **etl_s3_to_redshift**, **Runtime type** is **Python 3.12**, **Architecture** is **x84_64**. Select **Use an existing role** to set my lambda role was create before. Then click **Create function**.
    ![image](/images/Lambda/Lambda-to-Redshift/14.png)
    + Add lambda function code.
    + Select **Code** and paste the code source below before clicking **Deploy**.
    ```python
        import json
        import boto3
        import psycopg2 
        import base64


        def create_table_in_redshift(cursor):
            users_sql="""
            CREATE TABLE IF NOT EXISTS customers
            (
                customer_id int NOT NULL,
                name varchar(30),
                address varchar(50),
                phone varchar(20),
                age int,
                gender varchar(10),
                PRIMARY KEY(customer_id)
            )
            """
            cursor.execute(users_sql)
            
            products_sql="""
            CREATE TABLE IF NOT EXISTS products
            (
                product_id int NOT NULL,
                product_name varchar(30),
                price decimal,
                PRIMARY KEY (product_id)
            )
            """
            cursor.execute(products_sql)
            
            transactions_sql="""
            CREATE TABLE IF NOT EXISTS transactions
            (
                transaction_id int NOT NULL,
                customer_id int NOT NULL,
                product_id int NOT NULL,
                amount int,
                purchase_date datetime,
                total_price decimal,
                PRIMARY KEY(transaction_id),
                FOREIGN KEY(customer_id) REFERENCES customers(customer_id),
                FOREIGN KEY(product_id) REFERENCES products(product_id)
            )
            """
            cursor.execute(transactions_sql)

        def etl_function(row, cursor):
            """_summary_

            Args:
                row (json): containing the raw transaction data
            """
            
            # etl users data 
            customer_insert=f"""
                INSERT INTO customers VALUES(%d, '%s', '%s', '%s', %d, '%s')
            """%(row["customer_id"], row["name"], row["address"], row["phone number"], row["age"], row["gender"])
            cursor.execute(customer_insert)
            
            # etl product data 
            product_insert=f"""
                INSERT INTO products VALUES(%d, '%s', %f)
            """ % (row["product_id"], row["product_name"], row["price"])
            cursor.execute(product_insert)
            
            # etl transaction data 
            transaction_insert=f"""
                INSERT INTO transactions VALUES(%d, %d, %d, %d, '%s', %f)
            """ % (row['transaction_id'], row["customer_id"], row["product_id"], row["amount"], row['purchase_date'], row["amount"]*row["price"])
            cursor.execute(transaction_insert)



        def lambda_handler(event, context):
            # create connection to s3 
            bucket_name=event["Records"][0]["s3"]["bucket"]["name"]
            stream_key= event["Records"][0]["s3"]["object"]["key"]
            # # print(event)
            # print(bucket_name)
            # print(stream_key)
            # bucket_name="customer-datalake-quocbao"
            # stream_key="data-03-06-2024/event-05-04-17.json"
            
            s3_cli = boto3.client("s3")
            response=s3_cli.get_object(Bucket=bucket_name, Key=stream_key)
            raw_data= response["Body"].read().decode("utf-8")
            json_data = json.loads(raw_data)
            json_data = base64.b64decode(json_data["Records"][0]['kinesis']['data'])
            etl_data = json.loads(json_data)
            print(etl_data)
            try:
                conn = psycopg2.connect(
                    dbname='dev',
                    user='admin',
                    password='Password123',
                    host='quocbao-workgroup.211125538553.ap-south-1.redshift-serverless.amazonaws.com',
                    port='5439'  # or the correct port from Redshift console
                )
                
                cur = conn.cursor()
                
                create_table_in_redshift(cur)
                print(etl_data)
                etl_function(etl_data, cur)
                
                conn.commit()
                conn.close()
                return {"statusCode": 200, "body": "ETL data to redshift successful"}
            except Exception as e:
                return {"statusCode": 500, "body": str(e)}
    ```
    ![image](/images/Lambda/Lambda-to-Redshift/19.png)
2. Add **psycopg2** layer for lambda function
    + Create **psycopg_layer**
    + Select **Layer** then click **Create layer** to create new layer.
    ![image](/images/Lambda/Lambda-to-Redshift/15.png)
    + Set **Name** is **psycopg2_layer**, and upload [psycopg2_layer.zip](https://github.com/QuocBao02/AWS-Data-Pipeline/tree/main/Hugo_template_workshop/content/3-Lambda/Lambda-to-Redshift) file. Set **Architecture** is **x86_64** and **Runtime type** is **Python3.12**. Click **Create** to finish this step. 
    ![image](/images/Lambda/Lambda-to-Redshift/16.png)
    + Add layer for this lambda function
    ![image](/images/Lambda/Lambda-to-Redshift/17.png)
    + Select **Customer layer** and choose **psycopg2_layer** was created before. Then, click **Add**.
    ![image](/images/Lambda/Lambda-to-Redshift/18.png)

3. Add **VPC** for lambda function to connect **S3** and **Redshift**.
    + From the **Configuration** menu, select **VPC** and add our **default VPC, subnet, security groups**. Then, click **Add** to proceed to add VPC.
    ![image](/images/Lambda/Lambda-to-Redshift/22.png)
    ![image](/images/Lambda/Lambda-to-Redshift/23.png)
    ![image](/images/Lambda/Lambda-to-Redshift/24.png)
4. Add **S3** trigger for lambda function
    + From the **etl_s3_to_redshift** function of Lambda management console, click **Add trigger**
    ![image](/images/Lambda/Lambda-to-Redshift/25.png)
    + Choose **S3 source**
    ![image](/images/Lambda/Lambda-to-Redshift/26.png)
    + Set **Bucket** is **s3/customer-data-datalake-quocbao**, **Event types** are **PUT and POST**. Then, click **Add** to proceed to add S3 trigger for this lambda function.
    ![image](/images/Lambda/Lambda-to-Redshift/27.png)



