from .views import InvoiceViewSet, LastInvViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', InvoiceViewSet, basename='invoice')

urlpatterns = router.urls