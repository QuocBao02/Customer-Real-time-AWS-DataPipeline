from faker import Faker 
import time
import random
import boto3 
import json

# List of real product names
real_product_names = [
    "Apple iPhone 13",
    "Samsung Galaxy S21",
    "Sony WH-1000XM4 Headphones",
    "Dell XPS 13 Laptop",
    "Amazon Echo Dot",
    "Google Nest Hub",
    "Nintendo Switch",
    "PlayStation 5",
    "Xbox Series X",
    "Kindle Paperwhite",
    "Apple Watch Series 7",
    "Samsung Galaxy Tab S7",
    "Sony PlayStation VR",
    "GoPro HERO9",
    "Bose QuietComfort 35 II",
    "Canon EOS R5",
    "Nikon Z6 II",
    "DJI Mavic Air 2",
    "Fitbit Charge 5",
    "Garmin Forerunner 945"
]

def data_generator(fake, id):
    """
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
    """
    name = fake.name()
    address = fake.address()
    phone = fake.phone_number()
    age = fake.pyint(min_value=15, max_value = 70)
    gender = "M" if fake.pybool() else "F"
    product_name= random.choice(real_product_names)
    amount = fake.pyint(min_value=1, max_value= 150)
    price = fake.pyint(min_value=100, max_value=10000)
    purchase_date = fake.date()
    
    return {"customer_id": id, "name": name, "address": address, "phone number": phone, "age" : age, "gender": gender,"product_id":id, "product_name": product_name, "amount": amount, "price": price, "purchase_date": purchase_date, "transaction_id": id}

def send_data_to_kinesis(data, kinesis_cli, stream_name, partition_key):
    try:
        kinesis_cli.put_record(
            StreamName=stream_name,
            Data=json.dumps(data),
            PartitionKey=partition_key
        )
    except:
        print("Error sending data!")
        exit(1)


if __name__=="__main__":
    stream_name = "CustomersDataStream"
    partition_key="part_1"
    
    fake = Faker()
    kinesis_client = boto3.client("kinesis", region_name="ap-south-1")
    id = 1
    while True:
        data = data_generator(fake, id)
        send_data_to_kinesis(data, kinesis_client, stream_name, partition_key)
        print(f"Sent data: {data}")
        id +=1
        time.sleep(5)

