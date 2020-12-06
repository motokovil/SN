from rest_framework.routers import DefaultRouter
from .views import TagView

router = DefaultRouter()
router.register(f'', TagView)

urlpatterns = router.urls