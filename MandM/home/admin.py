

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'is_staff',
        'role'
        )
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups',
                )
        }),
        # ('Important dates', {
        #     'fields': ('last_login', 'date_joined')
        # }),
        ('Role', {
            'fields': ('role',)
        })
    )

admin.site.register(CustomUser, CustomUserAdmin)