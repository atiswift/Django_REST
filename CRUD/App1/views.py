from django.shortcuts import render
from rest_framework import viewsets
from .models import Employee
from .serializers import Employee_Serializer

class Employee_viewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = Employee_Serializer
