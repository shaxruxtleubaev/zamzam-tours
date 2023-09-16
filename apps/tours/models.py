from django.db.models import *

class Tour(Model):
    
    title = CharField(
        'Имя тура',
        max_length=256
    )

    price = CharField(
        'Цена тура',
        max_length=128
    )

    photo = ImageField(
        'Фото тура',
        upload_to='tours-photos'
    )

    def __str__(self):
        return f'{self.title}'
    
    class Meta:

        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'