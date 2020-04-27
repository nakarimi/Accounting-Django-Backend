from .views import InvoiceViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', InvoiceViewSet, basename='invoice')
urlpatterns = router.urls