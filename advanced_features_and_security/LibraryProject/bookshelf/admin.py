# LibraryProject/bookshelf/admin.py

from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'date_of_birth')

admin.site.register(CustomUser, CustomUserAdmin)
