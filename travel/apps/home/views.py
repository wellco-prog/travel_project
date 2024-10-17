from django.shortcuts import render
from django.views.generic import TemplateView
from ..post.models import Post
from ..accounts.models import User
from ..accounts.forms import SignUpForm
from django.views.generic import ListView
from django.views.generic import CreateView

# Create your views here.

class HomePageView(ListView):
    template_name = 'pages/home.html'
    model = Post
    context_object_name = 'post1'
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        # context['categories'] = Category.objects.all()
        context['last_post1'] = Post.objects.all()[:3]
        # context['post_tags'] = Tag.objects.all()
        # context['form'] = SearchForm(self.request.GET)
        # post = self.get_object()
        # context['comments'] = Comment.objects.filter(post=post)
        # context['comment_form'] = CommentsForm()
        return context

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'

class DestinationPageView(TemplateView):
    template_name = 'pages/destination.html'

class ServicePageView(TemplateView):
    template_name = 'pages/service.html'

class PackagePageView(TemplateView):
    template_name = 'pages/package.html'

class TestimonialPageView(TemplateView):
    template_name = 'pages/testimonial.html'

class GuidesPageView(TemplateView):
    template_name = 'pages/guide.html'



