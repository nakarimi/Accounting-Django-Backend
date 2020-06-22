from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from .models import Payment
from ..transaction.models import Transaction
from ..account.models import Account
from rest_framework import status
from rest_framework import viewsets
from .serializers import PaymentSerializer
from rest_framework.parsers import FileUploadParser, FormParser
from rest_framework.response import Response
from datetime import timedelta, datetime
import uuid 

# Create your views here.


class PaymentViewSet(viewsets.ViewSet):

  def list(self, request):

    start = self.request.query_params.get('start', None)
    if(start != None):
      end = self.request.query_params.get('end', None)
      end = datetime.strptime(end, "%Y-%m-%d") + timedelta(days=1)
      type = self.request.query_params.get('type', None)
      serializer = PaymentSerializer(
        Payment.objects.filter(
          created_at__range=[start, end],
          ),
        many=True)
    else:
      serializer = PaymentSerializer(
        Payment.objects.all(),
        many=True)
    return JsonResponse(serializer.data, safe=False)

  def retrieve(self, request, pk=None):

    # pay = Payment.objects.all()
    # pay = get_object_or_404(Payment, pk=pk)
    # serializer = PaymentSerializer(pay)
    # return JsonResponse(serializer.data, safe=False)
    return HttpResponse('True')

  def create(self, request):
    pay = PaymentSerializer(data=request.data)
    if pay.is_valid():
      instance = pay.save()

      # Create the transaction.
      Transaction.objects.create(
        type = instance.type,
        account = Account.objects.get(id=instance.account.id),
        payment = instance,
        amount = instance.amount,
      )

      return Response(pay.data, status=status.HTTP_201_CREATED)
    else:
      return Response({'error': pay.errors}, status=status.HTTP_400_BAD_REQUEST)

  def update(self, request, pk, *args, **kwargs):
    instance = get_object_or_404(Payment, id=pk)

    serializer = PaymentSerializer(data=request.data, instance=instance)
    if serializer.is_valid():
      serializer.save()

      # Create the transaction.
      Transaction.objects.filter(payment=instance.id).update(
        account = Account.objects.get(id=instance.account.id),
        type = instance.type,
        currency = instance.currency,
        amount = instance.amount,
      )

      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


  def partial_update(self, request, pk=None):
    return HttpResponse("Item Patched")

  def destroy(self, request, pk=None):
    instance = Payment.objects.filter(pk=pk)
    instance.delete()
    return HttpResponse('True')
