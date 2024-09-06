from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
class StudentModelViewSet1(viewsets.ModelViewSet):
    queryset  = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes =[IsAuthenticated]
    # http http://127.0.0.1:8000/studentapi/'Authorization:Bearer
#     # {
#     "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI1NTU5OTYxLCJpYXQiOjE3MjU1NTk2NjEsImp0aSI6IjJlZGIzZGZiZDNlMDQzYmFiMzI5NjViNzY4ZDQwNzIzIiwidXNlcl9pZCI6NH0.uyijf3bPAy-o_rgdzrtyTX9C1wzeeejmx6Gf9bAyGE8",
#     "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNTY0NjA2MSwiaWF0IjoxNzI1NTU5NjYxLCJqdGkiOiI4YjMxOTljYzVjZjk0MGIwYWM1ODZhZjNkZWEyMDcwYiIsInVzZXJfaWQiOjR9._Ox7XfEGcuwCbJ4ugE4GrEtcjRGqP30WHEFAJQyrQlc"
# }

# Get data with access token
# http http://127.0.0.1:8000/studentapi/ 'Authorization:Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI1NTYwNDg1LCJpYXQiOjE3MjU1NTk2NjEsImp0aSI6ImNjNmZiNDJmOTFkMDQzNzFiNWU1OWNjM2FjNDgxMTgwIiwidXNlcl9pZCI6NH0.c6Kh8sD2lrUUDbeAvs5qpl4MgtBgnUNF2bqO_8cnyoc'

#POST data with access token
# http -f POST http://127.0.0.1:8000/studentapi/ name=Biraj roll=103 city =Dhulikhel 'Authorization:Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI1NTU5OTYxLCJpYXQiOjE3MjU1NTk2NjEsImp0aSI6IjJlZGIzZGZiZDNlMDQzYmFiMzI5NjViNzY4ZDQwNzIzIiwidXNlcl9pZCI6NH0.uyijf3bPAy-o_rgdzrtyTX9C1wzeeejmx6Gf9bAyGE8'

#DELETE data with access token:
# http DELETE http://127.0.0.1:8000/studentapi/9/ 'Authorization:Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlCI6Mn0.Pwf0ejsWUC1w8vtZjzSynbx-huseMBQ5pXo5nq-x02M';c0d0527b-f2a7-430f-81bf-a5abc61dbd4aY2FhMGIxZTAxOGM4N2I2ODMwIiwidXNlcl9pZCI6Mn0.Pwf0ejsWUC1w8vtZjzSynbx-huseMBQ5pXo5nq-x02M'