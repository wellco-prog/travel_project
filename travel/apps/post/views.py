from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class BlogListPageView(TemplateView):
    template_name = 'pages/blog_list.html'

class BlogDetailPageView(TemplateView):
    template_name = 'pages/blog_details.html'