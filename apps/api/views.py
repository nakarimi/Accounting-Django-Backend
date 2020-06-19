from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from pytz import unicode
from rest_framework import viewsets
from apps.api.serializers import UserSerializer, GroupSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class UserIdViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)
        
class HelloView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        # Individual permissions
        # permissions = Permission.objects.filter(user=request.user)

        # Permissions that the user has via a group
        # group_permissions = Permission.objects.filter(group__user=request.user)
        content = {
            'user': unicode(request.user),
            'auth': unicode(request.auth),
        }

        return HttpResponse(content)
