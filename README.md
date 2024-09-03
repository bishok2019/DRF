Get user info with username and password
PS D:\New folder\DRF\tokenAuthentication> http POST http://127.0.0.1:8000/gettoken/ username="superuser" password="superuser"

Authentication using token
http http://127.0.0.1:8000/student-token/ 'Authorization:Token 28c89f82556240dbdc9a03c31c2fe9d4043eb23a'

create data after token auth
http -f POST  http://127.0.0.1:8000/studentapi/ name=Kamana roll=103 city=Hyderbad 'Authorization:Token 28c89f82556240dbdc9a03c31c2fe9d4043eb23a'
