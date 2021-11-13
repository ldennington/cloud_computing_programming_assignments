import json
import pandas as pd
from kafka import KafkaProducer

producer = KafkaProducer (bootstrap_servers=['129.114.27.100:30001'],
                         value_serializer=lambda x:
                         json.dumps(x).encode('utf-8'))

def publish(i):
    df = pd.read_csv('../resources/energy-sorted-part-2.csv',
        nrows=1000, skiprows=i, 
        names=['id', 'timestamp', 'value', 'property', 'plug_id', 'household_id', 'house_id'])
    data = df.to_json(orient="records")
    producer.send("Producer2", value=data)
    producer.flush()

for i in range(0, 500000, 1000):
    publish(i)

producer.close()
