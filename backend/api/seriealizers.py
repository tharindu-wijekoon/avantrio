from django.contrib.auth.models import User
from rest_framework import serializers
from .models import User_O

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_O
        fields = ["user_id", "email", "timestamp", "tasks"]
        
        def create(self,validated_data):
            print(validated_data)
            user = User_O.objects.create_user(**validated_data)
            return user