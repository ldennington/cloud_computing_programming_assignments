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
#    In this example, demonstrate Kafka streaming API to build a consumer.
#

import os
import time
from kafka import KafkaConsumer

consumer = KafkaConsumer (bootstrap_servers="129.114.25.169:9092")
consumer.subscribe (topics=["MeetUpSeattle", "MeetUpNewYork"])

for msg in consumer:
    print (str(msg.value, 'ascii'))

consumer.close ()