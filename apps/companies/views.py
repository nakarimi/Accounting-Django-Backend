from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, DjangoModelPermissions
from django.contrib.auth.models import User
from apps.companies.models import Company
from rest_framework import viewsets
from apps.companies.serializers import CompanySerializer
from rest_framework.parsers import FileUploadParser, FormParser
from .forms import CompanyForm

# Create your views here.


class CompanyViewSet(viewsets.ViewSet):
    parser_classes = [FormParser]
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
        # resutl = Company.objects.create(
        #     com_name = request.data['com_name'],
        #     com_email = request.data['com_email'],
        #     # com_logo = request.data['com_logo'],
        #     com_owner = request.data['com_owner'],
        #     com_status = request.data['com_status'],
        #     com_address = request.data['com_address'],
        #     com_phone = request.data['com_phone'],
        # )
        # return HttpResponse('resutl')
        # return HttpResponse(request.data, safe=False)
        company = CompanyForm(request.data, request.FILES)
        if company.is_valid():
            company = company.save()
            serializer = CompanySerializer(company)
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse(company.errors, safe=False)

    def update(self, request, pk):

        instance = get_object_or_404(Company, id=pk)
        company = CompanyForm(request.data, instance=instance)
        if company.is_valid():
            company = company.save()
            serializer = CompanySerializer(company)
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse(company.errors, safe=False)

    def partial_update(self, request, pk=None):
        return HttpResponse("Item Patched")

    def destroy(self, request, pk=None):
        instance = Company.objects.filter(pk=pk)
        instance.delete()
        return HttpResponse('True')
