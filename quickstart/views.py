# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
# Create your views here.

from .serializers import LoginSerializer
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import generics, mixins
from .serializers import Photo_GroupSerializer, PhotoSerializer
from .models import Photo_Group, Photo
from rest_framework.permissions import IsAuthenticated


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=200)


class LogoutView(APIView):
    authentication_classes = (TokenAuthentication, )

    def post(self, request):
        django_logout(request)
        return Response(status=204)




class Photo_GroupListView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = Photo_GroupSerializer
    queryset = Photo_Group.objects.all()
    # lookup_field = 'id'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk)
        else:
            return self.list(request)

#Not working
class PhotosByGroupIdListView(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = PhotoSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    #queryset = Photo.objects.all()

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        gid = self.kwargs['group']
        return Photo.objects.filter(gid=gid)

    # def get(self, request):
    #     gid = self.kwargs['group']
    #     return self.filter(gid=gid)


class PhotoListView(generics.GenericAPIView, mixins.RetrieveModelMixin):
    serializer_class = PhotoSerializer
    queryset = Photo.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        return self.retrieve(request, pk)