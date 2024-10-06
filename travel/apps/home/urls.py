from django.urls import  re_path, path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('destination/', DestinationPageView.as_view(), name='destination'),
    path('service/', ServicePageView.as_view(), name='service'),
    path('package/', PackagePageView.as_view(), name='package'),
    path('testimonial/', TestimonialPageView.as_view(), name='testimonial'),
    path('guide/', GuidesPageView.as_view(), name='guide'),
    path('sign_in/', SigninPageView.as_view(), name='sign_in'),
    path('sign_up/', SignupPageView.as_view(), name='sign_up'),
]