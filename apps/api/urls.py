from django.urls import path
from rest_framework import routers
from django.conf.urls import include, url
from .views import UserViewSet, UserIdViewSet
from . import views

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('cuser', views.UserIdViewSet)

urlpatterns = [
    path('', include(router.urls)),
]