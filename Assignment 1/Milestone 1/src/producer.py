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

import os   # need this for popen
import time # for
import requests
import json
from kafka import KafkaProducer  # producer of events

producer = KafkaProducer (bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         json.dumps(x).encode('utf-8'))

def get_stream(url):
    s = requests.Session()

    with s.get(url, headers=None, stream=True) as resp:
        for data in resp.iter_lines():
            if data:
                print(json.loads(data))
                producer.send ("MeetUp", value=json.loads(data))
                producer.flush()


for i in range (100):
    get_stream('https://stream.meetup.com/2/rsvps')
    time.sleep (5)

producer.close ()
