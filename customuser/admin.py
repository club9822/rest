from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('mobile', 'is_staff', 'is_active',)
    list_filter = ('mobile', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('mobile', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('mobile', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('mobile',)
    ordering = ('mobile',)


admin.site.register(CustomUser, CustomUserAdmin)
