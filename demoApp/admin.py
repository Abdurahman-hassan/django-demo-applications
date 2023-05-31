from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import MenuCategory, Menu, Demo

admin.site.register(MenuCategory)
admin.site.register(Menu)
admin.site.register(Demo)
# admin.site.unregister(User)

# @admin.register(User)
# class NewAdmin(BaseUserAdmin):
#     readonly_fields = ['date_joined']


class UserAdmin(BaseUserAdmin):
    # Define admin model for custom User model with non-email unique identifier field.
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'date_joined')
    readonly_fields = ['date_joined']
    search_fields = ("username__startswith", )

    def get_form(self, request, obj=None, **kwargs):
        """Return a custom form for the UserChange page.

        If the user is not a superuser, disable the username field."""

        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser

        if not is_superuser:
            form.base_fields['username'].disabled = True

        return form


    # Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
