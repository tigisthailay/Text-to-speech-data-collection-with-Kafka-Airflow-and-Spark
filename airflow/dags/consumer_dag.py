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
    logger.info("Consumer started")
    poll_timeout = 0
    while running:
        msg = c.poll(1.0)

        if poll_timeout == 20:
            running = False
            break

        if msg is None:
            poll_timeout = poll_timeout + 1
            print("No message received", poll_timeout)
            logger.debug("No message received")
        elif msg.error() is not None:
            logger.error(msg.error())
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

def insert_to_s3(**context):
    #fill the script to insert to S3
    print("insert_to_s3")

with DAG(
    dag_id="consumer_dag",
    schedule_interval="@daily",
    default_args={
        "owner": "airflow",
        "retries": 3,
        "retry_delay": timedelta(minutes=5),
        "start_date": datetime(2021, 1, 1),
    },
    catchup=False,
) as f:

    consumer_from_kafka = PythonOperator(
        task_id="consumer_from_kafka",
        python_callable=consumer_from_kafka,
        provide_context=True,
    )

    insert_to_s3 = PythonOperator(
        task_id="insert_to_s3",
        python_callable=insert_to_s3,
        provide_context=True,
    )

consumer_from_kafka >> insert_to_s3