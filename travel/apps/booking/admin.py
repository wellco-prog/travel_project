from django.contrib import admin
from .models import Destination, Package
# Register your models here.

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('naming',
                    'destination',
                    'daysCount',
                    'personsCount',
                    'image',
                    'price',
                    'offer',
                    'created_at',
                    'updated_at')


