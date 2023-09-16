from django.contrib.admin import *
from .models import Tour

@register(Tour)
class TourAdmin(ModelAdmin):

    list_display = ('id', 'title', 'price')
    list_display_links = ('id', 'title', 'price')
    ordering = ('-title',)