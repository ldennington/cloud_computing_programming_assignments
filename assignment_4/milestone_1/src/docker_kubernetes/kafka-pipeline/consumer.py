import requests
import yaml
import json
from kafka import KafkaConsumer

def read_db():
    with open("env.yml", "r") as stream:
        try:
            return (yaml.safe_load(stream))
        except yaml.YAMLError as exc:
            return (exc)

config = read_db()

consumer = KafkaConsumer (bootstrap_servers="129.114.27.100:9092",
                          value_deserializer=lambda m: json.loads(m.decode('utf-8')))
consumer.subscribe (topics=["Producer1", "Producer2"])

host = config['couchdb']['database_host']
port = config['couchdb']['database_port']
dbname = config['couchdb']['database_name']
user = config['couchdb']['database_user']
password = config['couchdb']['database_password']

for item in consumer:
    url     = f'http://{user}:{password}@{host}:{port}/{dbname}/_bulk_docs'
    payload = f'{{"docs": {item.value}}}'
    headers = {'Content-Type': 'application/json'}
    requests.post(url, data=payload, headers=headers)
consumer.close ()
