from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import KaizenUser

@admin.register(KaizenUser)
class KaizenUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'is_verified', 'verification_code']


