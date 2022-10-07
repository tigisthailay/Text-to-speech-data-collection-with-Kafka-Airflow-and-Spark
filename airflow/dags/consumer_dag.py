from datetime import timedelta
from airflow import DAG
from airflow import PythonOperator
from datetime import datetime
import pandas as pd
import boto3
import json
from kafka import KafkaConsumer, KafkaProducer
#from confluent_kafka.admin import AdminClient, NewTopic
from kafka.admin import KafkaAdminClient, NewTopic

from airflow.utils.dates import days_ago
from botocore.exceptions import ClientError
import logging
import os

BROKER_URL = ["b-1.batch6w7.6qsgnf.c19.kafka.us-east-1.amazonaws.com:9092",
              "b-2.batch6w7.6qsgnf.c19.kafka.us-east-1.amazonaws.com:9092"]

TOPIC = "null"

def consumer_from_kafka(**context):
    kafka_admin = KafkaAdminClient({"bootstrap.servers": BROKER_URL})
    """
    Consume messages from the topic
    Args:
        topic: The topic to consume from
    """

    c = KafkaConsumer(
        {
            "bootstrap.servers": BROKER_URL,
            "group.id": "121",
            "auto.offset.reset": "latest",
        }
    )
    messages = []
    c.subscribe([TOPIC])
    running = True
    # logger.info("Consumer started")
    poll_timeout = 0
    while running:
        msg = c.poll(1.0)

        if poll_timeout == 20:
            running = False
            break

        if msg is None:
            poll_timeout = poll_timeout + 1
            print("No message received", poll_timeout)
            # logger.debug("No message received")
        elif msg.error() is not None:
            # logger.error(msg.error())
            running = False

        else:
            poll_timeout = 0
            # Get the message from Kafka
            msg_value = msg.value()
            # decode the message
            msg_value = msg_value.decode("utf-8")
            messages.append(msg_value)

            print(f"Received message: {msg_value}")
    context["ti"].xcom_push(key="data", value=messages)

def insert_to_s3(file_name: str, bucket = '/mnt/10ac-batch-6/notebooks/josias_ounsinli', object_name=None):
    """If S3 object_name was not specified, use file_name"""
    if object_name is None:
        object_name = os.path.basename(file_name)

    """Upload the file"""
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

default_args = {
    'owner': 'Choquet-Bruhat',
    'depends_on_past': False,
    'email': ['josias.ouns.djossou@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=5),
}


with DAG(
    dag_id = 'consumer_dag',
    default_args=default_args,
    description='A DAG script that consumer from kafka and insert to s3',
    schedule_interval=timedelta(minutes=10),
    start_date=days_ago(1),
) as dag:
    
    cons_kafka = PythonOperator(
        task_id='from kafka', 
        python_callable=consumer_from_kafka)


    insert_s3 = PythonOperator(
        task_id='insert_s3', 
        python_callable=insert_to_s3)


    cons_kafka >> insert_s3