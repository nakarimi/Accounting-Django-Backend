from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from .models import Account
from rest_framework import viewsets
from .serializers import AccountSerializer
from rest_framework.parsers import FileUploadParser, FormParser
from .forms import AccountForm
# Create your views here.


class AccountViewSet(viewsets.ViewSet):

  def list(self, request):
    serializer = AccountSerializer(Account.objects.all(), many=True)
    return JsonResponse(serializer.data, safe=False)

  def retrieve(self, request, pk=None):

    # account = Account.objects.all()
    # account = get_object_or_404(Account, pk=pk)
    # serializer = AccountSerializer(account)
    # return JsonResponse(serializer.data, safe=False)
    return HttpResponse('True')

  def create(self, request):
    account = AccountForm(request.data)
    if account.is_valid():
      account = account.save()
      serializer = AccountSerializer(account)
      return JsonResponse(serializer.data, safe=False)
    else:
      return JsonResponse(account.errors, safe=False)

  def update(self, request, pk):
    # return HttpResponse("Item Patched")
    instance = get_object_or_404(Account, id=pk)
    account = AccountForm(request.data, instance=instance)
    if account.is_valid():
      account = account.save()
      serializer = AccountSerializer(account)
      return JsonResponse(serializer.data, safe=False)
    else:
      return JsonResponse(account.errors, safe=False)


  def partial_update(self, request, pk=None):
    return HttpResponse("Item Patched")

  def destroy(self, request, pk=None):
    instance = Account.objects.filter(pk=pk)
    instance.delete()
    return HttpResponse('True')
