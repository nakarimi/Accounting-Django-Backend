from .views import PaymentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', PaymentViewSet, basename='payment')

urlpatterns = router.urls