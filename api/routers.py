from rest_framework.routers import DefaultRouter

from api.views import CategorialViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'categorials', CategorialViewSet)
router.register(r'products', ProductViewSet)


urlpatterns = router.urls