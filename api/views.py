from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from pytz import unicode
from rest_framework import viewsets
from api.serializers import UserSerializer, GroupSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth.models import Permission
from django.contrib.auth.models import User
from pprint import pprint


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class HelloView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Individual permissions
        permissions = Permission.objects.filter(user=request.user)

        # Permissions that the user has via a group
        group_permissions = Permission.objects.filter(group__user=request.user)
        content = {
            'user': unicode(request.user),  # `django.contrib.auth.User` instance.
            'auth': unicode(request.auth),
            'permission': permissions,
            'group': group_permissions,# None
        }

        repr(content)
        # return content
