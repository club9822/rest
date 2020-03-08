from django.http import Http404
from django.shortcuts import render
from rest_framework import routers, serializers, viewsets, status
from rest_framework.response import Response
from rest_framework import mixins, generics
from user.models import User

from user.models import UserSerializer


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserProfile(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
