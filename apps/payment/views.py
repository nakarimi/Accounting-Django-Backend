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

# Create your views here.


class PaymentViewSet(viewsets.ViewSet):

  def list(self, request):
    serializer = PaymentSerializer(Payment.objects.all(), many=True)
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
        label = 'test',
        account = Account.objects.get(id=3),
        payment = instance,
        amount = 1000,
      )

      return Response(pay.data, status=status.HTTP_201_CREATED)
    else:
      return Response({'error': pay.errors}, status=status.HTTP_400_BAD_REQUEST)

  def update(self, request, pk, *args, **kwargs):
    instance = get_object_or_404(Payment, id=pk)

    serializer = PaymentSerializer(data=request.data, instance=instance)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


  def partial_update(self, request, pk=None):
    return HttpResponse("Item Patched")

  def destroy(self, request, pk=None):
    instance = Payment.objects.filter(pk=pk)
    instance.delete()
    return HttpResponse('True')