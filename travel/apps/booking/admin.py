from django.contrib import admin
from .models import Destination, Package, Order
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

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('package',
                    'from_date',
                    'user',
                    'created_at',
                    'updated_at'
                   )
