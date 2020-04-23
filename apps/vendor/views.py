from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from .models import Vendor
from rest_framework import viewsets
from .serializers import VendorSerializer
from rest_framework.parsers import FileUploadParser, FormParser
from .forms import VendorForm
# Create your views here.


class VendorViewSet(viewsets.ViewSet):

  def list(self, request):
    serializer = VendorSerializer(Vendor.objects.all(), many=True)
    return JsonResponse(serializer.data, safe=False)

  def retrieve(self, request, pk=None):

    # vendor = Vendor.objects.all()
    # vendor = get_object_or_404(Vendor, pk=pk)
    # serializer = VendorSerializer(vendor)
    # return JsonResponse(serializer.data, safe=False)
    return HttpResponse('True')

  def create(self, request):
    vendor = VendorForm(request.data)
    if vendor.is_valid():
      vendor = vendor.save()
      serializer = VendorSerializer(vendor)
      return JsonResponse(serializer.data, safe=False)
    else:
      return JsonResponse(vendor.errors, safe=False)
    # return HttpResponse('True')

  def update(self, request, pk):
    # return HttpResponse("Item Patched")
    instance = get_object_or_404(Vendor, id=pk)
    vendor = VendorForm(request.data, instance=instance)
    if vendor.is_valid():
      vendor = vendor.save()
      serializer = VendorSerializer(vendor)
      return JsonResponse(serializer.data, safe=False)
    else:
      return JsonResponse(vendor.errors, safe=False)


  def partial_update(self, request, pk=None):
    return HttpResponse("Item Patched")

  def destroy(self, request, pk=None):
    instance = Vendor.objects.filter(pk=pk)
    instance.delete()
    return HttpResponse('True')
