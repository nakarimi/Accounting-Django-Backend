from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from .models import Account
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import AccountSerializer
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class AccountViewSet(viewsets.ViewSet):
  parser_class = (FileUploadParser,)
  permission_classes = [IsAuthenticated]
  
  def list(self, request):
    serializer = AccountSerializer(Account.objects.all(), many=True)
    return JsonResponse(serializer.data, safe=False)

  def retrieve(self, request, pk=None):

    # account = Account.objects.all()
    # account = get_object_or_404(Account, pk=pk)
    # serializer = AccountSerializer(account)
    # return JsonResponse(serializer.data, safe=False)
    return HttpResponse('True')

  def create(self, request, *args, **kwargs):
    serializer = AccountSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def update(self, request, pk, *args, **kwargs):
    instance = get_object_or_404(Account, id=pk)

    serializer = AccountSerializer(data=request.data, instance=instance)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # instance = get_object_or_404(Account, id=pk)
    # account = AccountForm(request.data, instance=instance)
    # if account.is_valid():
    #   account = account.save()
    #   serializer = AccountSerializer(account)
    #   return JsonResponse(serializer.data, safe=False)
    # else:
    #   return JsonResponse({'error': account.errors}, safe=False)

  def partial_update(self, request, pk=None):
    instance = get_object_or_404(Account, id=pk)

    serializer = AccountSerializer(data=request.data, instance=instance)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def destroy(self, request, pk=None):
    instance = Account.objects.filter(pk=pk)
    instance.delete()
    return HttpResponse('True')
