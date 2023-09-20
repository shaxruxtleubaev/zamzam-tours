from django.db.models import *

class Video(Model):

    title = CharField(
        'Название видео',
        max_length=256
    )

    video = CharField(
        'Ссылка на видео',
        max_length=4096
    )

    def __str__(self):
        return f'{self.title}'
    
    class Meta:

        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'