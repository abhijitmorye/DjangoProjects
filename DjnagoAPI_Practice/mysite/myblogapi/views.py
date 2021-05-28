from django.shortcuts import render
from rest_framework import generics
from myapp.models import UserData
from .serializers import UserDataSerializer

# Create your views here.


class ListView(generics.ListCreateAPIView):
    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer


class UpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):

    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer
