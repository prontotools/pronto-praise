from django.contrib import admin

from .models import Praise


@admin.register(Praise)
class PraiseAdmin(admin.ModelAdmin):
    list_display = (
        'to',
        'by',
        'description',
        'created',
    )
