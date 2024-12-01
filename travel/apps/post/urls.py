from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('post', PostViewSet)
urlpatterns = [
    # path('', HomePageView.as_view(), name=''),
    path('', include(router.urls)),
    path('', include('rest_framework.urls')),
    path('blog_list/', BlogListPageView.as_view(), name='blog_list'),
    path('blog_details/<int:pk>/', BlogDetailPageView.as_view(), name='blog_details'),
    # blog_details указываем в html в команде  {% url 'blog_details'
    path('category/<slug:slug>', CategoryListView.as_view(), name='category_list'),
    path('tag/<slug:slug>', TagListView.as_view(), name='tag_list'),
    path('api/v1/post/', PostListCreateApiView.as_view(), name='post'),

    ]
