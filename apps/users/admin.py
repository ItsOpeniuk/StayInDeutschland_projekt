from django.contrib import admin
from django.utils import timezone
from apps.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'email', 'phone', 'is_lessor']
