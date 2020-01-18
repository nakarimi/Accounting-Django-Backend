from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import UserViewSet
from . import views

router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('test', views.HelloView.as_view()),
]