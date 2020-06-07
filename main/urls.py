"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('api/', include('apps.api.urls')),
    path('upload/', include('apps.uploadapp.urls')),
    path('acnt/', include('apps.account.urls')),
    path('csmr/', include('apps.customer.urls')),
    path('vdr/', include('apps.vendor.urls')),
    path('inv/', include('apps.invoice.urls')),
    path('itm/', include('apps.item.urls')),
    path('bitm/', include('apps.bill_item.urls')),
    path('bil/', include('apps.bill.urls')),
    path('last_inv/', include('apps.invoice.urls_last')),
    path('last_bil/', include('apps.bill.urls_last')),
    path('', admin.site.urls),
    path('auth/', obtain_auth_token),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

