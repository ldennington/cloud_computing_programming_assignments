#
#
# Author: Aniruddha Gokhale
# CS4287-5287: Principles of Cloud Computing, Vanderbilt University
#
# Created: Sept 6, 2020
#
# Purpose:
#
#    Demonstrate the use of Kafka Python streaming APIs.
#    In this example, we use the "top" command and use it as producer of events for
#    Kafka. The consumer can be another Python program that reads and dumps the
#    information into a database OR just keeps displaying the incoming events on the
#    command line consumer (or consumers)
#

import os
import time
import requests
import json
from kafka import KafkaProducer

# Chameleon IP: 129.114.25.169
# AWS IP: 54.196.220.28
producer = KafkaProducer (bootstrap_servers=[' 54.196.220.28:9092'],
                         value_serializer=lambda x:
                         json.dumps(x).encode('utf-8'))

def get_stream(url):
    s = requests.Session()

    with s.get(url, headers=None, stream=True) as resp:
        for data in resp.iter_lines():
            if data:
                city = json.loads(data)
                if city['group']['group_city'] == 'New York':
                    print(city)
                    producer.send ("MeetUpNewYork", value=city)
                    producer.flush()


for i in range (100):
    get_stream('https://stream.meetup.com/2/rsvps')
    time.sleep (1)

producer.close ()
