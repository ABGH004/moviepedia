from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


# Register your models here.
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = [
        "username",
        "first_name",
        "last_name",
        "email",
    ]
    list_editable = [
        "first_name",
        "last_name",
    ]
    list_per_page = 10

    search_fields = [
        "username",
    ]
