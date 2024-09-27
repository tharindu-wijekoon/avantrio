from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .seriealizers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import User_O

# Create your views here.
class CreateUserView(generics.CreateAPIView):
    queryset = User_O.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]