from django.urls import path
from .views import DestinationListView, PackageListView

urlpatterns = [
    path('destination/', DestinationListView.as_view(), name='destination'),
    path('package/<slug:slug>/', PackageListView.as_view(), name='package')
]