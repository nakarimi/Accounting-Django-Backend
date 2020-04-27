from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from .models import Invoice
from rest_framework import viewsets
from .serializers import InvoiceSerializer
from rest_framework.parsers import FileUploadParser, FormParser
from .forms import InvoiceForm
# Create your views here.


class InvoiceViewSet(viewsets.ViewSet):

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
    invoice = InvoiceForm(request.data)
    if invoice.is_valid():
      invoice = invoice.save()
      serializer = InvoiceSerializer(invoice)
      return JsonResponse(serializer.data, safe=False)
    else:
      return JsonResponse({'error': invoice.errors}, safe=False)

  def update(self, request, pk):
    # return HttpResponse("Item Patched")
    instance = get_object_or_404(Invoice, id=pk)
    invoice = InvoiceForm(request.data, instance=instance)
    if invoice.is_valid():
      invoice = invoice.save()
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
