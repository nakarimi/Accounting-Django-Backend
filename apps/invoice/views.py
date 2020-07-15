from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from .models import Invoice, Invoice_num
from rest_framework import status
from rest_framework import viewsets
from .serializers import InvoiceSerializer, InvoiceNumSerializer
from rest_framework.parsers import FileUploadParser, FormParser
from .forms import InvoiceForm
from rest_framework.response import Response
from ..item.models import Item
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class InvoiceViewSet(viewsets.ViewSet):

  permission_classes = [IsAuthenticated]

  def list(self, request):
    serializer = InvoiceSerializer(Invoice.objects.all(), many=True)
    return JsonResponse(serializer.data, safe=False)

  def retrieve(self, request, pk=None):

    # invoice = Invoice.objects.all()
    # invoice = get_object_or_404(Invoice, pk=pk)
    # serializer = InvoiceSerializer(invoice)
    # return JsonResponse(serializer.data, safe=False)
    return HttpResponse('True')

  def create(self, request):
    inv = InvoiceSerializer(data=request.data)
    if inv.is_valid():
      instance = inv.save()
      Invoice_num.objects.create(invoice=instance)
      return Response(inv.data, status=status.HTTP_201_CREATED)
    else:
      return Response(inv.errors, status=status.HTTP_400_BAD_REQUEST)

  def update(self, request, pk):
    # return HttpResponse("Item Patched")
    instance = get_object_or_404(Invoice, id=pk)
    invoice = InvoiceForm(request.data, instance=instance)
    if invoice.is_valid():
      invoice = invoice.save()

      # item = get_object_or_404(Item, invoice=instance.id)
      serializer = InvoiceSerializer(invoice)
      return JsonResponse(serializer.data, safe=False)
    else:
      return JsonResponse({'error': invoice.errors}, safe=False)


  def partial_update(self, request, pk=None):
    return HttpResponse("Item Patched")

  def destroy(self, request, pk=None):
    instance = Invoice.objects.filter(pk=pk)
    instance.delete()
    return HttpResponse('True')
  
class LastInvViewSet(viewsets.ViewSet):

  def list(self, request):
    serializer = InvoiceNumSerializer(Invoice_num.objects.last())
    return JsonResponse(serializer.data, safe=False)
