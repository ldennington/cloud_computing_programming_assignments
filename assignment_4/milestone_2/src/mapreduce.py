import json, requests, pandas as pd
from pyspark.sql import SparkSession

def get_data():
    r = requests.get('http://admin:password@129.114.27.100:30002/assignment_four/_all_docs?include_docs=true')
    data = [row['doc'] for row in r.json()['rows']]
    return pd.DataFrame(data)

def write_data(results):
    url     = 'http://admin:password@129.114.27.100:30002/assignment_four_averages/_bulk_docs'
    payload = f'{{"docs": {json.dumps(results)}}}'
    headers = {'Content-Type': 'application/json'}
    requests.post(url, data=payload, headers=headers)

if __name__ == "__main__":
    df = get_data()

    spark = SparkSession\
        .builder\
        .appName("MapReduceAverages")\
        .getOrCreate()
    
    zeroValues = (0,0,0,0)

    def seqOp(accumulator, element):
        if (element[0] == 0):
            return (accumulator[0] + element[1], accumulator[1] + 1, accumulator[2], accumulator[3])
        else:
            return (accumulator[0], accumulator[1], accumulator[2] + element[1], accumulator[3] + 1)

    def combOp(accumulator1, accumulator2):
        return (accumulator1[0] + accumulator2[0], accumulator1[1] + accumulator2[1], accumulator1[2] + accumulator2[2], accumulator1[3] + accumulator2[3])

    reduced = spark.createDataFrame(df) \
        .rdd.map(lambda x: ((x[8],x[7],x[6]), (x[5], x[4]))) \
        .aggregateByKey(zeroValues, seqOp, combOp) \
        .mapValues(lambda v: (v[0]/v[1], v[2]/v[3])) \
        .map(lambda x: {"key": x[0], "average_work": x[1][0], "average_load": x[1][1]}) \
        .collect()

    write_data(reduced)

    spark.stop()