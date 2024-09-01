from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here

# @api_view()
# def hello_world(request):
#     return Response({'msg':'Hello World'})
# @api_view(['GET','POST'])
# def hello_world(request):
#     return Response({'msg':'Hello World'})
@csrf_exempt
@api_view(['POST','GET'])
def hello_world(request):
    if request.method == "GET":
        print(request.data)
        return Response({'msg':'This is GET request'})
    
    if request.method == "POST":
        print(request.data)
        return Response({'msg':'This is POST request.', 'data':request.data})