from django.urls import path, include
from rest_framework import routers
from .views import MessageViewSet
from .views import MessageViewSet, UserViewSet
router = routers.DefaultRouter()
router.register(r'messages', MessageViewSet)
router.register(r'users', UserViewSet) 

urlpatterns = [
    path('', include(router.urls)),
]