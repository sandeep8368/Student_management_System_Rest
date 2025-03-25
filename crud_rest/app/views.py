from django.shortcuts import render
from rest_framework import viewsets
from app.serializers import studentSerializers
from app.models import studentModel

# Create your views here.
class studentViewSet(viewsets.ModelViewSet):
    queryset = studentModel.objects.all()
    serializer_class = studentSerializers