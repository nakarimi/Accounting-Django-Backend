from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', FileUploadView, basename='file')
urlpatterns = router.urls
# urlpatterns = [
#     path('', FileUploadView.as_view())
# ]