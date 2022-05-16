# from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from .serializers import EmployeeSerializer, ImageSerializer
from .models import Employees, Image


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all().order_by('id')
    serializer_class = EmployeeSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all().order_by('image')
    serializer_class = ImageSerializer