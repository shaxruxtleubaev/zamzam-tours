from django.contrib.admin import *
from .models import Tour

@register(Tour)
class TourAdmin(ModelAdmin):

    list_display = ('id', 'name', 'price')
    list_display_links = ('id', 'name', 'price')
    ordering = ('name',)