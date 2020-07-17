from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from .models import Customer
from rest_framework import viewsets
from .serializers import CustomerSerializer
from rest_framework.parsers import FileUploadParser, FormParser
from .forms import CustomerForm
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class CustomerViewSet(viewsets.ViewSet):
  permission_classes = [IsAuthenticated]

  def list(self, request):
    serializer = CustomerSerializer(Customer.objects.all(), many=True)
    return JsonResponse(serializer.data, safe=False)

  def retrieve(self, request, pk=None):

    # customer = Customer.objects.all()
    # customer = get_object_or_404(Customer, pk=pk)
    # serializer = CustomerSerializer(customer)
    # return JsonResponse(serializer.data, safe=False)
    return HttpResponse('True')

  def create(self, request):
    customer = CustomerForm(request.data)
    if customer.is_valid():
      customer = customer.save()
      serializer = CustomerSerializer(customer)
      return JsonResponse(serializer.data, safe=False)
    else:
      return JsonResponse({'error': customer.errors}, safe=False)
    # return HttpResponse('True')

  def update(self, request, pk):
    # return HttpResponse("Item Patched")
    instance = get_object_or_404(Customer, id=pk)
    customer = CustomerForm(request.data, instance=instance)
    if customer.is_valid():
      customer = customer.save()
      serializer = CustomerSerializer(customer)
      return JsonResponse(serializer.data, safe=False)
    else:
      return JsonResponse({'error': customer.errors}, safe=False)


  def partial_update(self, request, pk=None):
    return HttpResponse("Item Patched")

  def destroy(self, request, pk=None):
    instance = Customer.objects.filter(pk=pk)
    instance.delete()
    return HttpResponse('True')
