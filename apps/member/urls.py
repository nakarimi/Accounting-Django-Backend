from .views import MemberViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', MemberViewSet, basename='member')
urlpatterns = router.urls