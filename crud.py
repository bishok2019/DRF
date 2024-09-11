import requests
import json
URL="http://127.0.0.1:8000/studentapi/"

## Get Data
def student_get(id = None):
    data = {}
    headers = {'content-Type':'application/json'}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)    
    r = requests.get(url = URL, headers=headers, data = json_data)
    data = r.json()
    print(data)

# student_get()# leave empty then get all 

## Update
def update_data():
    
    data ={
    'id':6,
    # 'name': 'Raj',
    'roll':104,
    # 'city':'Udaypur'
    }
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.put(url = URL, headers=headers, data = json_data)
    data = r.json()
    print(data )
# update_data()

# Delete
def delete_data():
    
    data ={
    'id':4,
    }
    headers = {'content-Type':'application/json'}

    json_data = json.dumps(data)
    r = requests.delete(url = URL, headers=headers, data = json_data)
    data = r.json()
    print(data )

# delete_data()

# Create
def create_data():
    data ={
    # 'id':20,
    'name': 'Kendal',
    'roll':3,
    'city':'Luxumberg'}
    headers = {'content-Type':'application/json'}

    json_data = json.dumps(data)
    r = requests.post(url = URL, headers=headers, data = json_data)
    data = r.json()
    print(data)

    ## Update
def update_p_data():
    
    data ={
    'id':6,
    # 'name': 'Raju',
    'roll':104,
    # 'city':'Udaypur'
    }
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.patch(url = URL, headers=headers, data = json_data)
    data = r.json()
    print(data )
# update_data()

# student_get()
# create_data()
# update_p_data()
# update_data()
# delete_data()
student_get()