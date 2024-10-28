from django.views.generic import ListView
from .models import Destination, Package
from .forms import BookingForm
from django.shortcuts import render, redirect
# Create your views here.


class DestinationListView(ListView):
    model = Destination
    template_name = 'pages/destination.html'
    context_object_name = 'destinations'
    paginate_by = 3


class PackageListView(ListView):
    model = Package
    template_name = 'pages/package.html'
    context_object_name = 'packages'
    paginate_by = 3

    def get_queryset(self):
        return Package.objects.filter(
            destination__slug=self.kwargs['slug'])
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['booking_form'] = BookingForm()
        context['choices'] = Package.objects.all()
        return context

    # def my_view(request):
    #     if request.method == 'POST':
    #         form = BookingForm(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             return redirect('/')  # Замените на нужный URL
    #     else:
    #         form = BookingForm()
    #     return render(request, 'apps/package.html', {'form': form})
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['booking_form'] = Destination.objects.get(
    #         slug=self.kwargs['slug'])
    #     return context

