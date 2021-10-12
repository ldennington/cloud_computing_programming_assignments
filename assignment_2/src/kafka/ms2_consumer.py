import os
import time
from kafka import KafkaConsumer

consumer = KafkaConsumer (bootstrap_servers=" 129.114.25.169:9092")
consumer.subscribe (topics=["MeetUpSeattle", "MeetUpNewYork"])

for msg in consumer:
    print (str(msg.value, 'ascii'))

consumer.close ()
