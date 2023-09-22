from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User 


@admin.register(User)
class Admin(UserAdmin):
    list_display = ['phone', 'username', 'email', 'role']
    filter_horizontal = ()
    list_filter = ('is_active', 'role')
    fieldsets = ()
    search_fields = ('phone', 'email', 'last_name')
    list_display_links = ('username', 'email')
    # ordering = ('phone', 'email')
