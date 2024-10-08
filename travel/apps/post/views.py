from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Post, Category
# from .forms import CommentForm
# Create your views here.


class BlogListPageView(ListView):
    model = Post
    queryset = Post.objects.all().order_by('-created_at')
    template_name = 'pages/blog_list.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['last_post'] = Post.objects.all()[:3]
        return context






class BlogDetailPageView(DetailView):
    template_name = 'pages/blog_details.html'
    model = Post
    context_object_name = 'post'

class CategoryListView(ListView):
    model = Post
    template_name = 'pages/category_list.html'
    context_object_name = 'post_category'
    paginate_by = 3
    # queryset = Post.objects.filter(category__slug=self.kwarqs['slug'])
    def get_queryset(self):
        return Post.objects.filter(
            category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_post'] = Category.objects.filter(
            slug=self.kwargs['slug'])
        context['categories'] = Category.objects.all()
        context['last_post'] = Post.objects.all()[:3]
        return context