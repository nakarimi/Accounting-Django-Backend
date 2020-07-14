from .views import BillViewSet, LastBillViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', BillViewSet, basename='bill')

urlpatterns = router.urls