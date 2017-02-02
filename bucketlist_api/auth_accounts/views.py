# from django.shortcuts import render
# Create your views here.
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from auth_accounts.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer
