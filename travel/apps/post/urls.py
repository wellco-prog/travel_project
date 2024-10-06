from django.urls import  path
from .views import *

urlpatterns = [
    path('blog_list/', BlogListPageView.as_view(), name='blog_list'),
    path('blog_details/', BlogDetailPageView.as_view(), name='blog_details'),

]