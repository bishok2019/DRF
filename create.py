import requests
import json
URL="http://127.0.0.1:8000/studentapi/"

def create_data():
    data = [
    {'name': 'Eduardo', 'roll': 4, 'city': 'Aykhal'},
    {'name': 'Vinnie', 'roll': 5, 'city': 'Itaquyry'},
    {'name': 'Pablo', 'roll': 6, 'city': 'Ar Rawḑah'},
    {'name': 'Kristen', 'roll': 7, 'city': 'Bunga Mas'},
    {'name': 'Amelina', 'roll': 8, 'city': 'Wotho'},
    {'name': 'Thorin', 'roll': 9, 'city': 'Graksop'},
    {'name': 'Venita', 'roll': 10, 'city': 'Arlöv'},
    {'name': 'Felix', 'roll': 11, 'city': 'Nemyriv'},
    {'name': 'Morgana', 'roll': 12, 'city': 'Chicama'},
    {'name': 'Dione', 'roll': 13, 'city': 'Gaotai'},
    {'name': 'Martyn', 'roll': 14, 'city': 'Gajrug'},
    {'name': 'Aguste', 'roll': 15, 'city': 'Artybash'},
    {'name': 'Bob', 'roll': 16, 'city': 'San Jose'},
    {'name': 'Mauricio', 'roll': 17, 'city': 'Paulínia'},
    {'name': 'Mikey', 'roll': 18, 'city': 'Staropavlovskaya'},
    {'name': 'Chelsie', 'roll': 19, 'city': 'La Unión'},
    {'name': 'Elle', 'roll': 20, 'city': 'Mainri'},
    {'name': 'Giselbert', 'roll': 21, 'city': 'Manhan'},
    {'name': 'Lew', 'roll': 22, 'city': 'Gubuk Daya'},
    {'name': 'Jerrilyn', 'roll': 23, 'city': 'Liucheng'},
    {'name': 'Ange', 'roll': 24, 'city': 'Levandeira'},
    {'name': 'Vince', 'roll': 25, 'city': 'Kovrov'},
    {'name': 'Ilyse', 'roll': 26, 'city': 'Ostrów Mazowiecka'},
    {'name': 'Gareth', 'roll': 27, 'city': 'Dusun Desa Bunter'},
    {'name': 'Felicio', 'roll': 28, 'city': 'Sanguansi'},
    {'name': 'Sidney', 'roll': 29, 'city': 'Srostki'},
    {'name': 'Joni', 'roll': 30, 'city': 'Yuzhno-Sukhokumsk'},
    {'name': 'Suzanna', 'roll': 31, 'city': 'Skutskär'},
    {'name': 'Gerardo', 'roll': 32, 'city': 'Birsa'},
    {'name': 'Aguie', 'roll': 33, 'city': 'Stockholm'},
    {'name': 'Wendye', 'roll': 34, 'city': 'Besao'},
    {'name': 'Dorris', 'roll': 35, 'city': 'Chengnan'},
    {'name': 'Zorina', 'roll': 36, 'city': 'Sari'},
    {'name': 'Pepito', 'roll': 37, 'city': 'Nereta'},
    {'name': 'Melicent', 'roll': 38, 'city': 'Cartagena'},
    {'name': 'Carlos', 'roll': 39, 'city': 'Lamawan'},
    {'name': 'Dayna', 'roll': 40, 'city': 'Täby'},
    {'name': 'Germaine', 'roll': 41, 'city': 'Solotcha'},
    {'name': 'Hattie', 'roll': 42, 'city': 'Zangzhai'},
    {'name': 'Halie', 'roll': 43, 'city': 'Tumaco'},
    {'name': 'Jessika', 'roll': 44, 'city': 'Rouyuan'},
    {'name': 'Holt', 'roll': 45, 'city': 'Wukang'},
    {'name': 'Hallie', 'roll': 46, 'city': 'Palmas'},
    {'name': 'Siward', 'roll': 47, 'city': 'Cosmópolis'},
    {'name': 'Ingmar', 'roll': 48, 'city': 'Rizal'},
    {'name': 'Auberon', 'roll': 49, 'city': 'Myshkin'},
    {'name': 'Ula', 'roll': 50, 'city': 'Parajara'},
    {'name': 'Katy', 'roll': 51, 'city': 'Marsh Harbour'},
    {'name': 'Cherie', 'roll': 52, 'city': 'Yur’yev-Pol’skiy'},
    {'name': 'Worden', 'roll': 53, 'city': 'Tianyu'},
    {'name': 'Menard', 'roll': 54, 'city': 'Manūjān'},
    {'name': 'Lissa', 'roll': 55, 'city': 'Aniso'},
    {'name': 'Olag', 'roll': 56, 'city': 'Nyalindung'},
    {'name': 'Kelwin', 'roll': 57, 'city': 'Tafí del Valle'},
    {'name': 'Cele', 'roll': 58, 'city': 'Khombole'},
    {'name': 'Angelina', 'roll': 59, 'city': 'Tonantins'},
    {'name': 'Filip', 'roll': 60, 'city': 'Shijia'}
]
    headers = {'Content-Type': 'application/json'}
    
    for item in data:  # Iterate over each dictionary
        json_data = json.dumps(item)  # Convert dictionary to JSON
        r = requests.post(url=URL, headers=headers, data=json_data)  # Send each dictionary individually
        response_data = r.json()
    print(response_data)  # Print the response from the server for each request
create_data()