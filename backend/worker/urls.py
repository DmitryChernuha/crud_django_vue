from rest_framework import routers
from .views import WorkerViewSet

router = routers.DefaultRouter()

router.register('worker', WorkerViewSet)

urlpatterns = router.urls
