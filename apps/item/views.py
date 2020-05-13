from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from .models import Item
from rest_framework import viewsets
from .serializers import ItemSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser, FormParser
# Create your views here.


class ItemViewSet(viewsets.ViewSet):

  def list(self, request):
    queryset = Item.objects.all()
    inv_id = self.request.query_params.get('inv_id', None)
    if inv_id is not None:
        queryset = queryset.filter(invoice_id=inv_id)
    
    serializer = ItemSerializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False)

  def retrieve(self, request, pk=None):

    # invoice = Item.objects.all()
    # invoice = get_object_or_404(Item, pk=pk)
    # serializer = ItemSerializer(invoice)
    # return JsonResponse(serializer.data, safe=False)
    return HttpResponse('True')

  def create(self, request):
    item = ItemSerializer(data=request.data)
    if item.is_valid():
      instance = item.save()
      return Response(item.data, status=status.HTTP_201_CREATED)
    else:
      return Response(item.errors, status=status.HTTP_400_BAD_REQUEST)

  # def update(self, request, pk):
  #   # return HttpResponse("Item Patched")
  #   instance = get_object_or_404(Item, id=pk)
  #   invoice = ItemForm(request.data, instance=instance)
  #   if invoice.is_valid():
  #     invoice = invoice.save()
  #     serializer = ItemSerializer(invoice)
  #     return JsonResponse(serializer.data, safe=False)
  #   else:
  #     return JsonResponse({'error': invoice.errors}, safe=False)


  # def partial_update(self, request, pk=None):
  #   return HttpResponse("Item Patched")

  # def destroy(self, request, pk=None):
  #   instance = Item.objects.filter(pk=pk)
  #   instance.delete()
  #   return HttpResponse('True')