from django.contrib import admin
from signup.models import KaizenUser

@admin.register(KaizenUser)
class KaizenUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'is_verified', 'verification_code']


