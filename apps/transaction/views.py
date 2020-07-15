from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from .models import Transaction
from rest_framework import status
from rest_framework import viewsets
from .serializers import TransactionSerializer
from rest_framework.parsers import FileUploadParser, FormParser
from rest_framework.response import Response
from django.db.models import Count, Sum
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class TransactionViewSet(viewsets.ViewSet):

  permission_classes = [IsAuthenticated]
  
  def list(self, request):

    data = Transaction.objects.all()

    serializer = TransactionSerializer(data, many=True)
    return JsonResponse(serializer.data, safe=False)

  def retrieve(self, request, pk=None):

    # transaction = Transaction.objects.all()
    # transaction = get_object_or_404(Transaction, pk=pk)
    # serializer = TransactionSerializer(transaction)
    # return JsonResponse(serializer.data, safe=False)
    return HttpResponse('True')
    
class LastTransactionViewSet(viewsets.ViewSet):

  def list(self, request):
    serializer = TransactionNumSerializer(Transaction.objects.last())
    return JsonResponse(serializer.data, safe=False)
