from django.db.models import *

class Video(Model):

    title = CharField(
        'Название видео',
        max_length=256
    )

    video = FileField(
        'Видео',
        upload_to='videos/'
    )

    def __str__(self):
        return f'{self.title}'
    
    class Meta:

        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'