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
from django.conf.urls import url, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    url(r'^api/password-reset/',
        include('django_rest_resetpassword.urls', namespace='password_reset')),

    path('', admin.site.urls),
    path('auth/', obtain_auth_token),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/', include('apps.api.urls')),
    path('api/upload/', include('apps.uploadapp.urls')),
    path('api/trs/', include('apps.transaction.urls')),
    path('api/pay/', include('apps.payment.urls')),
    path('api/acnt/', include('apps.account.urls')),
    path('api/csmr/', include('apps.customer.urls')),
    path('api/memb/', include('apps.member.urls')),
    path('api/vdr/', include('apps.vendor.urls')),
    path('api/inv/', include('apps.invoice.urls')),
    path('api/itm/', include('apps.item.urls')),
    path('api/bitm/', include('apps.bill_item.urls')),
    path('api/bil/', include('apps.bill.urls')),
    path('api/last_inv/', include('apps.invoice.urls_last')),
    path('api/last_bil/', include('apps.bill.urls_last')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

