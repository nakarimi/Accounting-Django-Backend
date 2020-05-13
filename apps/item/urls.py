from .views import ItemViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ItemViewSet, basename='item')
urlpatterns = router.urls