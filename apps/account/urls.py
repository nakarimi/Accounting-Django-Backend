from .views import AccountViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', AccountViewSet, basename='account')
urlpatterns = router.urls