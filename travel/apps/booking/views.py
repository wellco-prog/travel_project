import datetime

import requests
from django.http import JsonResponse, HttpResponse
from django.views.generic import ListView, DetailView
from rest_framework import generics, mixins, viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import Destination, Package
from .forms import BookingForm
from django.shortcuts import render, redirect

from .serializers import PackageSerializer
from .token_telegram_bot import TOKEN
from ..accounts.custom_permission import IsAdminOrReadOnly
from ..post.views import PostPagePagination


# Create your views here.
class BookViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
    ):  # ModelViewSet
    queryset = Package.objects.all().order_by('-created_at')
    serializer_class = PackageSerializer
    pagination_class = PostPagePagination
    permission_classes = [IsAdminOrReadOnly]

    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    # @action(methods=['get'], detail=False)
    # def category(self, request):
    #     cats = Destination.objects.all().values()
    #     return Response({'cats': [cats]})

class DestinationListView(ListView):
    model = Destination
    template_name = 'pages/destination.html'
    context_object_name = 'destination'
    paginate_by = 3


class BookingListCreateApiView(generics.ListCreateAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    # pagination_class = PostPagePagination


class BookingPagePagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'page_size'
    max_page_size = 100


class PackageListView(ListView):
    model = Package
    form_class = BookingForm
    template_name = 'pages/package.html'
    context_object_name = 'packages'
    paginate_by = 3

    # def get_queryset(self):
    #     return Package.objects.filter(
    #         destination__slug=self.kwargs['slug'])
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['booking_form'] = BookingForm()
        # context['choices'] = Package.objects.all()
        return context
    # def bookorder(self, request, *args, **kwargs):
    #     form = BookingForm(request.POST)
    #     if form.is_valid():
    #         order = form.save(commit=False)
    #         order.package = self.get_object()
    #         order.from_date = self.get_object()
    #         order.user = request.user
    #         order.save()
    #         return redirect('package/', )
    #     return self.render_to_response(self.get_context_data(form=form))
    def post(self, request, *args, **kwargs):
        telegram_bot_token = TOKEN
        telegram_chat_id = '-1002404354142'#'-1002212310184'

        form = BookingForm(request.POST)
        if form.is_valid():
             # Сохраняем данные из формы
            order = form.save(commit=False)
             # Добавляем текущего пользователя к заказу
            order.user = request.user
            order.save()  # Сохраняем в базе данных

            id = request.POST.get('naming')
            name = Package.objects.filter(id=id).first()
            date = request.POST.get('from_date')
            author = request.user
            email = request.user.email

            # Форматируем сообщение
            message = f"Новая заявка:\nАккаунт: {author}\nИмя пакета: {name}\nДата отправки: {date}\nEmail: {email}"
            # Отправляем сообщение в Telegram
            url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage"
            data = {
                "chat_id": telegram_chat_id,
                "text": message
            }
            response = requests.post(url, data=data)
            return JsonResponse({'status': 'success', 'message': 'Спасибо за заказ! Мы скоро свяжемся с Вами!'})
        else:
            # return self.render_to_response(self.get_context_data(form=form))
            return JsonResponse({'status': 'error', 'message': 'Ошибка! Заполните форму!'})
        #     form = BookingForm()
        #     return render(request, 'pages/package.html', {'form': form})


    # def my_view(request):
    #     if request.method == 'POST':
    #         form = BookingForm(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             return redirect('/')  # Замените на нужный URL
    #     else:
    #         form = BookingForm()
    #     return render(request, 'apps/packages.html', {'form': form})
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['booking_form'] = Destination.objects.get(
    #         slug=self.kwargs['slug'])
    #     return context


