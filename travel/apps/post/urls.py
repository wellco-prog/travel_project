from django.urls import  path
from .views import *

urlpatterns = [
    path('blog_list/', BlogListPageView.as_view(), name='blog_list'),
    path('blog_details/<int:pk>/', BlogDetailPageView.as_view(), name='blog_details'), # blog_details указываем в html в команде  {% url 'blog_details'
    path('category/<slug:slug>', CategoryListView.as_view(), name='category_list'),
    path('tag/<slug:slug>', TagListView.as_view(), name='tag_list')

]