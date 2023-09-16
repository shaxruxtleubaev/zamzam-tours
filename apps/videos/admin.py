from django.contrib.admin import *
from .models import Video

@register(Video)
class VideoAdmin(ModelAdmin):

    list_display = ('id', 'title')
    list_display_links = ('id', 'title')