from rest_framework import viewsets
from .models import Message
from .serializers import MessageSerializer
from django.contrib.auth.models import User
from .serializers import MessageSerializer, UserSerializer

# API pour les messages
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

   
from django.contrib.auth.models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer