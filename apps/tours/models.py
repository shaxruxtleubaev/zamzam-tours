from django.db.models import *

class Tour(Model):
    
    name = CharField(
        'Имя тура',
        max_length=256
    )

    price = CharField(
        'Цена тура',
        max_length=256
    )

    photo = CharField(
        'Ссылка фото тура',
        # upload_to='tours-photos'
        max_length=4096
    )

    places_amount = CharField(
        'Количество мест', 
        max_length=256
    )

    hotel_name = CharField(
        'Имя отеля',
        max_length=256
    )

    hotel_link = CharField(
        'Ссылка к отелю',
        max_length=256
    )

    def __str__(self):
        return f'{self.name}'
    
    class Meta:

        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'