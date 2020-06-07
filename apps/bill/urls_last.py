from .views import BillViewSet, LastBillViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', LastBillViewSet, basename='last_bill')
urlpatterns = router.urls