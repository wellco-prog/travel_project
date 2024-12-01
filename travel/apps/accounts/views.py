from django.views import View
from django.views.decorators.http import require_http_methods
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render, redirect
from .forms import *
from django.views.generic import CreateView, FormView
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse

# Create your views here.
class SignupPageView(CreateView):
    template_name = 'pages/sign_up.html'
    model = User
    form_class = SignUpForm
    success_url = '/packages/'

class SignInView(FormView):
    model = User
    form_class = SignInForm
    template_name = 'pages/sign_in.html'

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        user = authenticate(username=username,
                            email=email,
                            password=password
                            )

        if user is not None:
            if user.is_active:
                login(self.request, user)
                return redirect('home')
            else:
                return HttpResponse('Disabled account')
        else: HttpResponse('Invalid login')

# @require_http_methods(['GET','POST'])
def logout2(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('home')
    return redirect('home')


# class LogoutView(APIView):
#     def get(self, request):
#         if request.user.is_authenticated:
#             logout(request)
#             return redirect('home')
#
#     def post(self, request):
#         if request.user.is_authenticated:
#             logout(request)
#             return redirect('home')


class ExampleView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)