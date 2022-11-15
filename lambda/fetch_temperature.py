import json, requests
import boto3

from config import *

my_bucket = 'temperature-pipeline'
s3 = boto3.client(   's3',
                    aws_access_key_id = IAM_ACCESS_KEY,
                    aws_secret_access_key = IAM_SECRET_KEY)

def upload(json_path, json_data, csv_path, csv_buffer):
    s3.put_object(Body=json.dumps(json_data), Bucket=my_bucket, Key=json_path, ContentType='application/json')
    s3.put_object(Body=csv_buffer.getvalue(), Bucket=my_bucket, Key=csv_path)
    print('csv uploaded successfully')

def get_data():
    url = "https://api.open-meteo.com/v1/forecast?latitude=39.77&longitude=-74.26&hourly=temperature_2m"
    
    resp = requests.get(url)
    json_object = json.dumps(resp.text, indent=4)
    
    with open("sample.json", "w") as outfile:
        outfile.write(json_object)

get_data()