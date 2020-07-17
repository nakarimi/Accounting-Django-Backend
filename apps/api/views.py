from django.shortcuts import render

from django.contrib.auth.models import User, Group
from pytz import unicode
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from apps.api.serializers import UserSerializer, GroupSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.decorators import action
from .forms import UserForm
from rest_framework import status
from rest_framework.response import Response



# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(
        methods=['post'],
        detail=False,
        url_path='update',
        url_name='update',
    )
    def userChangePass(self, request, *args, **kwargs):
        user = User.objects.get(pk=self.request.user.id)
        user = UserForm(request.data, instance=user)
        if user.is_valid():
            user = user.save()
            serializer = UserSerializer(user)
            if(request.data['password']):
                if(user.check_password(request.data['oldpassword'])):
                    user.set_password(request.data['password'])
                    user.save()
                    return JsonResponse(serializer.data, safe=False)
                else:
                    return Response({'Authentication': 'Wrong password.'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return JsonResponse(serializer.data, safe=False)
        else:
            return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(
        methods=['post'],
        detail=False,
        url_path='reset-pass',
        url_name='reset-pass',
    )
    def userResetPass(self, request, *args, **kwargs):
        user = User.objects.get(username=request.data['username'])
        if (user):
            user.set_password(request.data['password'])
            user = user.save()
            return JsonResponse("Password Changed", safe=False)
        else:
            return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)

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
