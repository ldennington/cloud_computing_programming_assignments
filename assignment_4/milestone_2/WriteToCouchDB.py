import json
import requests
import os
import fnmatch


class WriteToCouchDB:
    def run():
        #Create DB
        requests.put('http://admin:password@129.114.27.100:30002/spark_output')

        url     = f'http://admin:password@129.114.27.100:30002/spark_output/'
        headers = {'Content-Type': 'application/json'}
        files = {}

        #Get output files
        for filename in os.listdir('.'):
            if fnmatch.fnmatch(filename, 'output-*.txt'):
                files[filename[:12]] = filename

        #Read files and build JSON to send to DB
        for file in files:
            f = open(files[file],"r")
            lines = f.readlines()

            for line in lines:
                parse = line.split(",")
                row = {
                    "house_id":parse[0].replace('(', '').strip() + "_" + parse[1].strip() + "_" + parse[2].replace(')', '').strip(),
                    "avg":parse[3].replace(')', '').strip()
                }
                payload = f'{{"doc": {json.dumps(row)}}}'
                requests.post(url, data=payload, headers=headers)
        
