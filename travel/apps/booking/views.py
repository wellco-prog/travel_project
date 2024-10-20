from django.views.generic import ListView
from .models import Destination, Package

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
