from rest_framework.routers import DefaultRouter
from .views import ComentarioView
router = DefaultRouter()
router.register(f'', ComentarioView)

urlpatterns = router.urls