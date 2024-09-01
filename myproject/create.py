import requests
import json
URL="http://127.0.0.1:8000/studentapi/"
data ={
    # 'id':11,
    'name': 'Antony',
    'roll':11,
    'city':'Texas'
}

json_data = json.dumps(data)
r = requests.post(url = URL, data = json_data)
data = r.json()
print(data)