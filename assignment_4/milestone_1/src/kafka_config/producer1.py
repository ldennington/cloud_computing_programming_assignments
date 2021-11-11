import json
import pandas as pd
from kafka import KafkaProducer

producer = KafkaProducer (bootstrap_servers=['127.0.0.1:9092'],
                         value_serializer=lambda x:
                         json.dumps(x).encode('utf-8'))
def publish(i):
    # df = pd.read_csv('../resources/test.csv',
    #     nrows=5, skiprows=i, 
    #     names=['id', 'timestamp', 'value', 'property', 'plug_id', 'household_id', 'house_id'])
    # data = df.to_json(orient="index")
    # parsed = json.loads(data)
    with open('./out.json') as file:
        data = json.load(file)
    
    for item in data:
        print(data.get(item))
        # for data in item:
        #     print(data)
           # print(json.loads(data))

        # f = json.load(file)
        # f.update(parsed)
        # file.seek(0)
        # json.dump(data, file)
    # producer.send("Producer1", value=data)
    # producer.flush()

for i in range(0, 10, 5):
    publish(i)

producer.close()