from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, DjangoModelPermissions
from django.contrib.auth.models import User
from companies.models import Company
from rest_framework import viewsets
from companies.serializers import CompanySerializer

# Create your views here.


class CompanyViewSet(viewsets.ViewSet):
    permission_classes = [
        # IsAuthenticated,
        # IsAuthenticatedOrReadOnly,
        DjangoModelPermissions,
    ]
    queryset = User.objects.none()  # Required for DjangoModelPermissions

    def list(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return JsonResponse(serializer.data, safe=False)

    def retrieve(self, request, pk=None):
        companies = Company.objects.all()
        company = get_object_or_404(companies, pk=pk)
        serializer = CompanySerializer(company)
        return JsonResponse(serializer.data, safe=False)

    def create(self, request):
        return HttpResponse("Item Created with Post method")

    def update(self, request, pk=None):
        return HttpResponse("Item updated with put method")

    def partial_update(self, request, pk=None):
        return HttpResponse("Item Patched")

    def destroy(self, request, pk=None):
        return HttpResponse("it will delete")
