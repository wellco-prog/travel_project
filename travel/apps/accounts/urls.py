from django.urls import path, include, re_path
from .views import *
from rest_framework import routers

urlpatterns = [
    path('auth/', include('rest_framework.urls')),
    path('sign_up/', SignupPageView.as_view(), name='sign_up'),
    path('sign_in/', SignInView.as_view(), name='sign_in'),
    path('logout1/', logout2, name='logout'),

]
