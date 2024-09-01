import requests
import json
URL="http://127.0.0.1:8000/studentapi/"
def update_data():
    
    data ={
    'id':14,
    # 'name': 'Riya',
    # 'roll':121,
    'city':'Manchester'
    }

    json_data = json.dumps(data)
    r = requests.put(url = URL, data = json_data)
    data = r.json()
    print(data )

update_data()