from django.core.management import BaseCommand
from django.core.management.color import no_style
from django.db import connection

from flowers.models import Category
from flowers.models import Flowers

sequence_sql = connection.ops.sequence_reset_sql(no_style(), [Category, Flowers])
with connection.cursor() as cursor:
    for sql in sequence_sql:
        cursor.execute(sql)


class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {'name': 'Пионовые (Paulowniaceae) ',
             'description': 'Многолетнее растение с несколькими стеблями (стволами) высотой до 1 м. Листья непарно '
                            'перисто раздельные или тройчатые. Одиночные крупные цветы простые, махровые или '
                            'полуметровые. Имеют цвет белый, кремовый, оттенки розового, малиновый, бордовый.'},
            {'name': 'Розовые (Aerospace)',
             'description': 'Растение имеет форму куста. Высота от 30 до 200 см. Стебли '
                            'одеревесневающие с шипами. Цветы простые, полу махровые или'
                            'махровые всех цветов и оттенков, кроме черного и синего.'},
            {'name': 'Бобовые (Fabrice)',
             'description': 'Вечнозеленый кустарник высотой 60-80 см, иногда до 150 см. '
                            'На небольших веточках куста располагаются мелкие листья, '
                            'а соцветия образуют метелки из цветочков, имеющих форму '
                            'шариков ярко желтого цвета.'},
            {'name': 'Лилейные (Celiac)',
             'description': 'Растение имеет высоту от 60 до 80 см, широкие листья, '
                            'крупные цветки бокаловидной формы. Существует множество '
                            'сортов тюльпанов. Окраска также разнообразна: все '
                            'оттенки красного, желтого, розового, лилового.'}
        ]
        category_for_create = []
        for item in category_list:
            category_for_create.append(
                Category(**item)
            )

        Category.objects.bulk_create(category_for_create)

    pk_1 = Category.objects.get(pk=1)
    pk_2 = Category.objects.get(pk=2)
    pk_3 = Category.objects.get(pk=3)
    pk_4 = Category.objects.get(pk=4)

    flowers_list = [
        {'name': 'Пион', 'category': pk_1, 'price': 100.50},
        {'name': 'Роза', 'category': pk_2, 'price': 120.40},
        {'name': 'Мимоза', 'category': pk_3, 'price': 90.00},
        {'name': 'Тюльпан', 'category': pk_4, 'price': 45.00}
    ]

    product_for_create = []
    for item in flowers_list:
        product_for_create.append(
            Flowers(**item)
        )
    Flowers.objects.bulk_create(product_for_create)
