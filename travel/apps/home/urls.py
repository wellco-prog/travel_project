from django.urls import  path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about', AboutPageView.as_view(), name='about'),
    path('contact', ContactPageView.as_view(), name='contact'),
    path('destination', DestinationPageView.as_view(), name='destination'),
    path('service', ServicePageView.as_view(), name='service'),
    path('package', PackagePageView.as_view(), name='package'),
]