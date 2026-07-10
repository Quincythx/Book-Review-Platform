from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'is_verified', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('bio', 'is_verified')}),
    )


admin.site.register(User, CustomUserAdmin)