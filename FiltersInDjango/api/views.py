from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from .models import Student
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

# Per view
class studentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend] 
    filterset_fields = ['city','name']
    # filterset_fields = ['city']
# Global View
# class studentList(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     filterset_fields = ['city']

# class studentList(ListAPIView):
#     queryset = Student.objects.filter(passby='User_8')
#     serializer_class = StudentSerializer

# class studentList(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class studentList(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     def get_queryset(self):
#         user = self.request.user
#         return Student.objects.filter(passby=user)