from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from core import models

# https://docs.djangoproject.com/en/2.2/ref/contrib/admin/
class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    # control which fields are displayed on the change list page of the admin
    list_display = ['email', 'name']
    # control the layout of admin "add" and "change" pages
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (_('Permissions'),{'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (_('Important dates'), {'fields': ('last_login',)})
    )

admin.site.register(models.User, UserAdmin)

