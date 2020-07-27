from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from .models import Member
from rest_framework import viewsets
from .serializers import MemberSerializer
from rest_framework.parsers import FileUploadParser, FormParser
from .forms import MemberForm
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
# Create your views here.


class MemberViewSet(viewsets.ViewSet):
  permission_classes = [IsAuthenticated]

  def list(self, request):
    serializer = MemberSerializer(Member.objects.all(), many=True)
    return JsonResponse(serializer.data, safe=False)

  def retrieve(self, request, pk=None):

    # member = Member.objects.all()
    # member = get_object_or_404(Member, pk=pk)
    # serializer = MemberSerializer(member)
    # return JsonResponse(serializer.data, safe=False)
    return HttpResponse('True')

  def create(self, request):
    member = MemberForm(request.data)
    if member.is_valid():
      member = member.save()
      serializer = MemberSerializer(member)

      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(member.errors, status=status.HTTP_400_BAD_REQUEST)
    #   return JsonResponse(serializer.data, safe=False)
    # else:
    #   return JsonResponse({'error': member.errors}, safe=False)
    # return HttpResponse('True')

  def update(self, request, pk):
    # return HttpResponse("Item Patched")
    instance = get_object_or_404(Member, id=pk)
    member = MemberForm(request.data, instance=instance)
    if member.is_valid():
      member = member.save()
      serializer = MemberSerializer(member)
      return JsonResponse(serializer.data, safe=False)
    else:
      return JsonResponse({'error': member.errors}, safe=False)


  def partial_update(self, request, pk=None):
    return HttpResponse("Item Patched")

  def destroy(self, request, pk=None):
    instance = Member.objects.filter(pk=pk)
    instance.delete()
    return HttpResponse('True')
