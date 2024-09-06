from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from api.customauth import CustomAuthentication

# Session Authentication
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminUser]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [IsAuthenticated]

# Basic Authentication
class StudentModelViewSet2(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [BasicAuthentication]

# User as Admin and Superuser can Retirive and Modify data with Token after TokenAuthentication
class token_auth(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticatedOrReadOnly]

# get user info with username and password
# PS D:\New folder\DRF\tokenAuthentication> http POST http://127.0.0.1:8000/gettoken/ username="superuser" password="superuser"


#  Authentication using token
#GET
# http http://127.0.0.1:8000/student-token/ 'Authorization:Token 28c89f82556240dbdc9a03c31c2fe9d4043eb23a'


# put data with token auth
#UPDATE
# http -f  PUT  http://127.0.0.1:8000/student-token/4/ name=Keisha roll=104 city=Sidney 'Authorization:Token 28c89f82556240dbdc9a03c31c2fe9d4043eb23a'

class Custom_Auth(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]