from django.urls import path, include
from rest_framework import routers

from .views import DestinationListView, PackageListView, BookingListCreateApiView, BookViewSet

router = routers.DefaultRouter()
router.register('post', BookViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('', include('rest_framework.urls')),
    path('destination/', DestinationListView.as_view(), name='destination'),
    path('package/', PackageListView.as_view(), name='packaging'),
    path('api/v1/booking/', BookingListCreateApiView.as_view(), name='booking'),

    ]
