from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from .models import Bill, Bill_num
from rest_framework import status
from rest_framework import viewsets
from .serializers import BillSerializer, BillNumSerializer
from rest_framework.parsers import FileUploadParser, FormParser
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class BillViewSet(viewsets.ViewSet):

  permission_classes = [IsAuthenticated]

  def list(self, request):
    serializer = BillSerializer(Bill.objects.all(), many=True)
    return JsonResponse(serializer.data, safe=False)

  def retrieve(self, request, pk=None):

    # bill = Bill.objects.all()
    # bill = get_object_or_404(Bill, pk=pk)
    # serializer = BillSerializer(bill)
    # return JsonResponse(serializer.data, safe=False)
    return HttpResponse('True')

  def create(self, request):
    bill = BillSerializer(data=request.data)
    if bill.is_valid():
      instance = bill.save()
      Bill_num.objects.create(bill=instance)
      return Response(bill.data, status=status.HTTP_201_CREATED)
    else:
      return Response({'error': bill.errors}, status=status.HTTP_400_BAD_REQUEST)

  def update(self, request, pk, *args, **kwargs):
    instance = get_object_or_404(Bill, id=pk)

    serializer = BillSerializer(data=request.data, instance=instance)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


  def partial_update(self, request, pk=None):
    return HttpResponse("Item Patched")

  def destroy(self, request, pk=None):
    instance = Bill.objects.filter(pk=pk)
    instance.delete()
    return HttpResponse('True')
  
class LastBillViewSet(viewsets.ViewSet):

  def list(self, request):
    serializer = BillNumSerializer(Bill_num.objects.last())
    return JsonResponse(serializer.data, safe=False)
