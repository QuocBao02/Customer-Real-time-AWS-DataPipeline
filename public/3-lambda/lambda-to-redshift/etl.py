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
    
    