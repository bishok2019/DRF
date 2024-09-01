import requests
import json
URL="http://127.0.0.1:8000/studentapi/"
def delete_data():
    
    data ={
    'id':2,
    }

    json_data = json.dumps(data)
    r = requests.delete(url = URL, data = json_data)
    data = r.json()
    print(data )

delete_data()