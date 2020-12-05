from rest_framework.routers import DefaultRouter
from .views import PublicacionView
router = DefaultRouter()
router.register(f'', PublicacionView)

urlpatterns = router.urls