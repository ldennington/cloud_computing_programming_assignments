
import requests
import json

class FetchCouchDb:
    def call_db():
        r = requests.get('http://admin:password@129.114.27.100:30002/assignment_four/_all_docs?include_docs=true')
        rows = [];
        for i in r.json()['rows']:
            rows.append({
                'id': i['doc']['id'],
                'timestamp': i['doc']['timestamp'],
                'value': i['doc']['value'],
                'property': i['doc']['property'],
                'plug_id': i['doc']['plug_id'],
                'household_id': i['doc']['household_id'],
                'house_id': i['doc']['house_id']
            })
        with open('./input.json', 'w', encoding='utf-8') as f:
            json.dump(rows, f, ensure_ascii=False, indent=4)
