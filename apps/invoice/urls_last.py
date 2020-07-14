from .views import InvoiceViewSet, LastInvViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', LastInvViewSet, basename='last_invoice')
urlpatterns = router.urls