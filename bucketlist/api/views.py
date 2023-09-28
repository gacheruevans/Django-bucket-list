from django.shortcuts import render
from rest_framework import generics

from .models import User, Bucketlist
from .serializers import UserSerializer, BucketlistSerializer


class UserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CreateBucketListView(generics.CreateAPIView):
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer


class BucketListView(generics.ListAPIView):
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
