import requests, json
from datetime import datetime
from flask import Flask, render_template, Response

def dish_sent_to_core(request, test_mode=False, output_dir="/tmp/"):

    if test_mode == False:
        request_args = request.args
        record_id = request_args['record_id']
    else:
        record_id = '62927'

    headers = {
        'QB-Realm-Hostname': 'thecbrgroup',
        'Authorization': 'QB-USER-TOKEN b35r4c_i55j_ckefttbcpxmvqmcbkyjpubtw4yvj'
    }
    body = {
        "to": "brqrdp78k",
        "data": [
            {
                "3": {
                    "value": int(record_id)
                },
                "239": {
                    "value": 1
                },
                "242": {
                    "value": str(datetime.now().date())#.strftime('%m-%d-%Y')
                }
            }
        ]
    }
    r = requests.post(
    'https://api.quickbase.com/v1/records', 
    headers = headers, 
    json = body
    )

    print(json.dumps(r.json(),indent=4))


    if test_mode == False:
        # Redirect
        return render_template('index.html', record_id = record_id)
  
if __name__ == '__main__':
    dish_sent_to_core(None, True, "tmp/")