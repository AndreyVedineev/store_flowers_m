# Generated by Django 4.2.3 on 2023-07-25 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0002_blog_fl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_fl',
            name='number_of_views',
            field=models.IntegerField(blank=True, null=True, verbose_name='Количество просмотров'),
        ),
    ]