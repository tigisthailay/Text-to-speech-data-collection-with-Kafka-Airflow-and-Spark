import json
import boto3
import pandas as pd

from flask import Flask, jsonify, make_response, request
from flask_cors import CORS
from kafka import KafkaProducer

# from confluent_kafka import Consumer, Producer
# from confluent_kafka.admin import AdminClient, NewTopic

app = Flask(__name__)
CORS(app)

BROKER_URL = ["b-1.batch6w7.6qsgnf.c19.kafka.us-east-1.amazonaws.com:9092",
              "b-2.batch6w7.6qsgnf.c19.kafka.us-east-1.amazonaws.com:9092"]
TOPIC = "null"


@app.route("/gettext", methods=["GET"])
def get_text():
    s3 = boto3.client("s3")

    bucket = "Our bucketname"

    response = s3.get_object(Bucket=bucket, Key="location to csv")

    status = response.get("ResponseMetadata", {}).get("HTTPStatusCode")

    if status == 200:
        print(f"Status - {status}")
        df = pd.read_csv(response.get("article"))
        single_random_text = df.sample(n=1)["headline"]
        single_random_text.reset_index(drop=True, inplace=True)
        print(single_random_text)
        print({"staus": "sucess", "data": single_random_text[0].strip()})

    else:
        print(f"Status - {status}")
        return make_response(
            jsonify(
                {
                    "status": "fail",
                }
            ),
            400,
        )


    producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode("utf-8"))
    producer.send("null", {"text": single_random_text[0].strip()})

    return make_response(
        jsonify({"success": True, "data": single_random_text[0].strip()}), 200
    )


if __name__ == "__main__":
    app.run(host="localhost", port=11000, debug=False)
