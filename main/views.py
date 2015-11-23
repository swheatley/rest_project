from django.shortcuts import render
from rest_framework import generics
from main.models import Phone
from main.serializers import PhoneSerializer


class PhoneList(generics.ListAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer



