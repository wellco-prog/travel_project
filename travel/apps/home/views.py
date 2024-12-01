from django.views.generic import TemplateView
from ..post.models import Post
from .models import Contact
from ..booking.models import Package
from django.views.generic import ListView, CreateView
from .forms import ContactForm

# Create your views here.


class ContactPageView(CreateView):
    template_name = 'pages/contact.html'
    model = Contact
    context_object_name = 'contact'
    form_class = ContactForm
    success_url = '/contact'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['contact'] = ContactForm()
    #     return context

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


class DestinationPageView(TemplateView):
    template_name = 'pages/destination.html'

class ServicePageView(TemplateView):
    template_name = 'pages/service.html'

# class PackagePageView(TemplateView):
#     template_name = 'pages/package.html'

class PackageListView(ListView):
    model = Package
    template_name = 'pages/package.html'
    context_object_name = 'packages'
    paginate_by = 3

class TestimonialPageView(TemplateView):
    template_name = 'pages/testimonial.html'

class GuidesPageView(TemplateView):
    template_name = 'pages/guide.html'



