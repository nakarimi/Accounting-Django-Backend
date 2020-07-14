from .views import Bill_itemViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', Bill_itemViewSet, basename='bill_item')
urlpatterns = router.urls