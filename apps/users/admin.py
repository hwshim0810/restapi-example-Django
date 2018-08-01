from django.contrib import admin

from . import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email',
        'name',
        'is_staff',
        'is_superuser',
        'created_at',
    )
    list_display_links = (
        'id',
        'email',
        'name',
    )
    list_filter = (
        'is_staff',
        'is_superuser',
        'created_at',
    )
    fieldsets = (
        (None, {
            'fields': (
                'email',
                'name',
                'job',
                'followers',
                'following',
            )
        }),
        ('Permissions', {
            'fields': (
                'is_staff',
                'is_superuser',
            )
        }),
        ('Dates', {
            'fields': (
                'created_at',
            )
        })
    )
    search_fields = (
        'email',
        'name',
    )
    readonly_fields = (
        'email',
        'created_at',
    )
