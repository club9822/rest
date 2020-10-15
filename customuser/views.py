from django.http import Http404
from django.shortcuts import render
from rest_framework import routers, serializers, viewsets, status
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import mixins, generics
from customuser.models import CustomUser
from django.shortcuts import get_object_or_404
from customuser.models import UserSerializer


#
#
# # ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()


#
#
class UserProfileView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    # def
    # def get(self, request, pk, *args, **kwargs):
    #     print(request.user)
    #     if (request.user.id == pk or request.user.is_staff == True):
    #         user = CustomUser.objects.get(self, id=pk)
    #         return Response(UserSerializer(user))
    #     return Response(data='no user')
    # items = get_object_or_404(ItemBatch, id=self.kwargs.get('pk'))
    # serializer = holdSerializer(items)
    # return Response(serializer.data)
