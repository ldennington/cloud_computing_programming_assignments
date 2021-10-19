import os
import time
import requests
import json
from kafka import KafkaProducer

producer = KafkaProducer (bootstrap_servers=['129.114.27.100:9092'],
                         value_serializer=lambda x:
                         json.dumps(x).encode('utf-8'))

def get_stream(url):
    s = requests.Session()

    with s.get(url, headers=None, stream=True) as resp:
        for data in resp.iter_lines():
            if data:
                city = json.loads(data)
                print(city['group']['group_city'])
                if city['group']['group_city'] == 'Seattle':
                    print(city)
                    producer.send ("MeetUpSeattle", value=city)
                    producer.flush()


for i in range (100):
    get_stream('https://stream.meetup.com/2/rsvps')
    time.sleep (1)

producer.close ()
