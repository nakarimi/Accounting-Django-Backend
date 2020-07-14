from .views import TransactionViewSet, LastTransactionViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', TransactionViewSet, basename='transaction')

urlpatterns = router.urls