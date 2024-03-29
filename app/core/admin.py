from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# this hook is needed to make django projects translatable,
# Wrap the texts with this if you want django to automatically translate
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
    # fields to be included in add user page
    # therefore we can create a new user with email and password
    add_fieldsets = (
        (None, {
            #Two useful classes defined by the default admin site stylesheet are collapse and wide. 
            #Fieldsets with the collapse style will be initially collapsed in the admin and 
            #replaced with a small “click to expand” link. Fieldsets with the wide style will 
            #be given extra horizontal space.
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )
# https://www.mlr2d.org/contents/djangorestapi/05_modifying_djangoadmininterface
admin.site.register(models.User, UserAdmin)

