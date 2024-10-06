from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

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

class SigninPageView(TemplateView):
    template_name = 'pages/sign_in.html'

class SignupPageView(TemplateView):
    template_name = 'pages/sign_up.html'