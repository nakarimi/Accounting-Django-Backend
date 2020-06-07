from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from .models import Bill_item
from rest_framework import viewsets
from .serializers import Bill_itemSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser, FormParser
# Create your views here.


class Bill_itemViewSet(viewsets.ViewSet):

  def list(self, request):
    queryset = Bill_item.objects.all()
    bill_id = self.request.query_params.get('entity_id', None)
    if bill_id is not None:
        queryset = queryset.filter(bill_id=bill_id)
    
    serializer = Bill_itemSerializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False)

  def retrieve(self, request, pk=None):

    # vendor = Bill_item.objects.all()
    # vendor = get_object_or_404(Bill_item, pk=pk)
    # serializer = Bill_itemSerializer(vendor)
    # return JsonResponse(serializer.data, safe=False)
    return HttpResponse('True')

  def create(self, request):
    bill_item = Bill_itemSerializer(data=request.data)
    if bill_item.is_valid():
      instance = bill_item.save()
      return Response(bill_item.data, status=status.HTTP_201_CREATED)
    else:
      return Response({'error': bill_item.errors})

  # def update(self, request, pk):
  #   # return HttpResponse("Bill_item Patched")
  #   instance = get_object_or_404(Bill_item, id=pk)
  #   vendor = Bill_itemForm(request.data, instance=instance)
  #   if vendor.is_valid():
  #     vendor = vendor.save()
  #     serializer = Bill_itemSerializer(vendor)
  #     return JsonResponse(serializer.data, safe=False)
  #   else:
  #     return JsonResponse({'error': vendor.errors}, safe=False)


  # def partial_update(self, request, pk=None):
  #   return HttpResponse("Bill_item Patched")

  def destroy(self, request, pk=None):
    instance = Bill_item.objects.filter(pk=pk)
    instance.delete()
    return HttpResponse('True')