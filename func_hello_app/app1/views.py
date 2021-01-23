from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def hello_world(request):
    if request.method == "POST":
        return Response(request.data)
    return Response("Hello World",status=status.HTTP_200_OK)
