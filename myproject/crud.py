import requests
import json
URL="http://127.0.0.1:8000/studentapi/"

## Get Data
def student_get(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)    
    r = requests.get(url = URL, data = json_data)
    data = r.json()
    print(data)

# student_get()# leave empty then get all 

## Update
def update_data():
    
    data ={
    'id':22,
    'name': 'Everest',
    # 'roll':198,
    'city':'tjbhjj'
    }

    json_data = json.dumps(data)
    r = requests.put(url = URL, data = json_data)
    data = r.json()
    print(data )
# update_data()

# Delete
def delete_data():
    
    data ={
    'id':30,
    }

    json_data = json.dumps(data)
    r = requests.delete(url = URL, data = json_data)
    data = r.json()
    print(data )

delete_data()

# Create
def create_data():
    data ={
    # 'id':20,
    'name': 'Everes',
    'roll':196,
    'city':'Solu'
}

    json_data = json.dumps(data)
    r = requests.post(url = URL, data = json_data)
    data = r.json()
    print(data)

# create_data()
student_get()