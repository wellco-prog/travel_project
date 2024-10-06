from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(User)
class UserTextAdmin(admin.ModelAdmin):
    list_display = [
        'username',
        'email',
        'avatar',
        'about',
        'birth_date',
        # 'phone',
        'city',
        'gender'
    ]