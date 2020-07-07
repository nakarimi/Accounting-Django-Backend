from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from .models import Payment
from ..transaction.models import Transaction
from ..account.models import Account
from ..bill.models import Bill
from ..invoice.models import Invoice
from ..account.serializers import AccountSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import PaymentSerializer
from rest_framework.parsers import FileUploadParser, FormParser
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
      curr = self.request.query_params.get('curr', None)
      serializer = PaymentSerializer(
        Payment.objects.filter(
          created_at__range=[start, end],
          currency=curr,
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
      newPay = pay.save()
      accnt = Account.objects.get(id=newPay.account.id);
      # Create the transaction.
      Transaction.objects.create(
        type = newPay.type,
        account = accnt,
        payment = newPay,
        amount = newPay.amount,
      )

      # Update Account balance.
      newBalance = 0;
      if(newPay.type == "Income"):
        newBalance = accnt.balance + newPay.amount
      else:
        newBalance = accnt.balance - newPay.amount

      Account.objects.filter(id=newPay.account.id).update(
        balance= newBalance,
      )

      #update Invoice/Bill Balance
      newBalance = 0;
      if(newPay.type == "Income"):
        # This is Invoice.
        inv = Invoice.objects.get(id=pay.data['ref_inv']);
        newBalance = inv.balance - newPay.amount
        Invoice.objects.filter(id=pay.data['ref_inv']).update(
          balance= newBalance,
        )

      else:
        # This is Bill.
        inv = Bill.objects.get(id=pay.data['ref_bill']);
        newBalance = bill.balance - newPay.amount
        Bill.objects.filter(id=pay.data['ref_bill']).update(
          balance= newBalance,
        )

      return Response(pay.data, status=status.HTTP_201_CREATED)
    else:
      return Response(pay.errors, status=status.HTTP_400_BAD_REQUEST)

  def update(self, request, pk, *args, **kwargs):
    pay = get_object_or_404(Payment, id=pk)
    oldAmount = pay.amount
    oldAccnt = pay.account
    oldType = pay.type
    oldRefBill = pay.ref_bill
    oldRefInv = pay.ref_inv

    serializer = PaymentSerializer(data=request.data, instance=pay)
    if serializer.is_valid():
      upPay = serializer.save()

      # return Response(upPay.ref_inv, status=status.HTTP_201_CREATED)
      # Create the transaction.
      Transaction.objects.create(
        type = upPay.type,
        account = upPay.account,
        payment = upPay,
        amount = upPay.amount,
      )

      if(oldAccnt.id == upPay.account.id):
        newBalance = 0;
        if(pay.type == "Income"):
          newBalance = oldAccnt.balance + (upPay.amount - oldAmount)
        else:
          newBalance = oldAccnt.balance - (upPay.amount + oldAmount)

        Account.objects.filter(id=oldAccnt.id).update(
          balance= newBalance,
        )
      else:
        newBalance = 0;
        if(oldType == "Income"):
          newBalance = oldAccnt.balance - oldAmount
        else:
          newBalance = oldAccnt.balance + oldAmount

        Account.objects.filter(id=oldAccnt.id).update(
          balance= newBalance,
        )

        Transaction.objects.create(
          type = upPay.type,
          account = oldAccnt,
          payment = upPay,
          amount = oldAmount,
        )
        # Update new account
        newBalance = 0;
        accnt = Account.objects.get(id=upPay.account.id);
        if(pay.type == "Income"):
          newBalance = accnt.balance + pay.amount
        else:
          newBalance = accnt.balance - pay.amount

        Account.objects.filter(id=upPay.account.id).update(
          balance= newBalance,
        )

              #update Invoice/Bill Balance
      newBalance = 0;
      if(upPay.type == "Income"):
        # This is Invoice.

        inv = Invoice.objects.get(id=upPay.ref_inv.id);
        newBalance = inv.balance - (upPay.amount + oldAmount)
        return Response(newBalance, status=status.HTTP_201_CREATED)

        Invoice.objects.filter(id=upPay.ref_inv.id).update(
          balance= newBalance,
        )

      else:
        # This is Bill.
        inv = Bill.objects.get(id=upPay.ref_bill.id);
        newBalance = bill.balance - upPay.amount
        Bill.objects.filter(id=upPay.ref_bill.id).update(
          balance= newBalance,
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
