from django.core.management import BaseCommand
from django.core.management.color import no_style
from django.db import connection

from flowers.models import Blog_fl


sequence_sql = connection.ops.sequence_reset_sql(no_style(), [Blog_fl])
with connection.cursor() as cursor:
    for sql in sequence_sql:
        cursor.execute(sql)


class Command(BaseCommand):

    def handle(self, *args, **options):
        blog_list = [
            {'name': 'Желтые цветы: лесные цветы с желтым оттенком, дикие желтые розы.',
             'content': 'Желтый тон часто появляется в лесу. Желтые цветы, вероятно, относятся к самой видовой '
                        'группе, когда дело доходит до цветных цветов, которые можно найти в лесу. Во время '
                        'прогулки по лесу стоит посмотреть на деревья, под папоротниками и другими уголками леса, '
                        'потому что здесь, возможно, прячутся некоторые из этих экземпляров.',
             'is_publication': True},
            {'name': 'Многолетние красивые цветы белого цвета',
             'content': 'Почвопокровные растения, или растения, которые разрастаются и покрывают землю, '
                        'часто используются для борьбы с эрозией на склонах или как простая в уходе замена дерновой '
                        'траве.',
             'is_publication': False},
            {'name': 'Цветы пента - шикарные большие живые букеты.',
             'content': 'Цветы пента (Pentas lanceolata) известны под разными названиями, включая звездчатые гроздья, '
                        'пентас и египетские звездчатые цветы.',
             'is_publication': True},
        ]
        blog_for_create = []
        for item in blog_list:
            blog_for_create.append(Blog_fl(**item))

            Blog_fl.objects.bulk_create(blog_for_create)
