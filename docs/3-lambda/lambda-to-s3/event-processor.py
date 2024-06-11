import json
import boto3
import time


def generate_partition():
    '''Create directory to save data into data lake in hadoop hdfs'''
    current_time=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    date_string = current_time.split()[0].split('-')
    time_string = current_time.split()[1].split(':')
    year=date_string[0]
    month=date_string[1]
    day=date_string[2]
    hour=time_string[0]
    minute=time_string[1]
    second=time_string[2]
    
    prefix = "data-" + day + "-" + month + "-" + year + "/"
    data="event-"+hour+"-"+minute+"-"+second+".json"
    return prefix+data


s3_cli = boto3.client("s3")
bucket_name = "customer-data-datalake-quocbao"

def lambda_handler(event, context):
    object_name = generate_partition()
    # print(event)
    # print(object_name)
    s3_cli.put_object(
            Bucket=bucket_name,
            Key=object_name,
            Body=json.dumps(event).encode("utf-8")
    )
    return {
        'statusCode': 200
    }
    
