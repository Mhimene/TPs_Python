from rest_framework import serializers
from .models import Message

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
        
# Convertir Message en JSON
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['source', 'to', 'body']

