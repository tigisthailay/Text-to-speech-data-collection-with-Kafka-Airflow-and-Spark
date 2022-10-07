from datetime import timedelta
from textwrap import dedent
from kafka import KafkaConsumer
from time import sleep
import numpy as np
import io

import boto3
s3 = boto3.resource('s3')

from airflow import DAG

# Operators
#from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator

default_args = {
    'owner': 'Choquet-Bruhat',
    'depends_on_past': False,
    'email': ['josias.ouns.djossou@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=5),
}

def kafka_to_s3():
    consumer = KafkaConsumer('morawetz_audio_topic',
    client_id='d_id',
    bootstrap_servers=['b-1.batch6w7.6qsgnf.c19.kafka.us-east-1.amazonaws.com:9092,b-2.batch6w7.6qsgnf.c19.kafka.us-east-1.amazonaws.com:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=False)
    
    for event in consumer:
        s3.meta.client.upload_file('provide file path', '/mnt/10ac-batch-6/notebooks/josias_ounsinli', 'object name')
        print("Saved in bucket successfully!")

with DAG(
    'audio',
    default_args=default_args,
    description='A DAG script that schedules audio',
    schedule_interval=timedelta(minutes=10),
    start_date=days_ago(1),
    tags=['audio'],
) as dag:
    
    src_s3 = PythonOperator(
        task_id='kafka_to_s3', 
        python_callable=kafka_to_s3, 
        dag=dag)

    src_s3