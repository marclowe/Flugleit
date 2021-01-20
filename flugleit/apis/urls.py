#apis/urls.py
from django.urls import path

# from .views import ListStudent, DetailStudent

from .views import FlightViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', FlightViewSet, basename='flights')
urlpatterns = router.urls