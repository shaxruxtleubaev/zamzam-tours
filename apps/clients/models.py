from django.db.models import *

class Client(Model):

    fullname = CharField(
        'ФИО',
        max_length=256
    )

    date_of_birth = DateField(
        'Дата рождения',
        max_length=256
    )

    country = CharField(
        'Страна',
        max_length=256
    )

    passport_data = CharField(
        'Серия и номер паспорта',
        max_length=256
    )

    phone_number = CharField(
        'Телефон номер',
        max_length=256
    )

    tour_name = CharField(
        'Имя тура',
        max_length=256
    )

    tour_price = CharField(
        'Цена тура',
        max_length=256
    )

    def __str__(self):
        return f'{self.fullname}'
    
    class Meta:

        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'