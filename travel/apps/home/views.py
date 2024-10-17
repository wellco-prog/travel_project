from django.views.generic import TemplateView
from ..post.models import Post
from django.views.generic import ListView

# Create your views here.

class HomePageView(ListView):
    template_name = 'pages/home.html'
    model = Post
    context_object_name = 'post1'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['last_post1'] = Post.objects.all()[:3]
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



