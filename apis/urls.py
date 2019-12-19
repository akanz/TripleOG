from django.urls import path
from .views import InfoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', InfoViewSet, basename= 'info')
urlpatterns = router.urls