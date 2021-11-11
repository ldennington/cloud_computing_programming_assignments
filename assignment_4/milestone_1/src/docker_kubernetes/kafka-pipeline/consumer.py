import couchdb
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

consumer = KafkaConsumer (bootstrap_servers="127.0.0.1:9092")
consumer.subscribe (topics=["Producer1", "Producer2"])

host = config['couchdb']['database_host']
port = config['couchdb']['database_port']
dbname = config['couchdb']['database_name']
user = config['couchdb']['database_user']
password = config['couchdb']['database_password']

couchserver = couchdb.Server("http://%s:%s@%s:%s/" % (user, password, host, port))

db = couchserver[dbname]

for item in consumer:
    db.save(item, batch='ok')
consumer.close ()