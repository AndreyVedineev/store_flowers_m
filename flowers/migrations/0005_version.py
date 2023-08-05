# Generated by Django 4.2.3 on 2023-08-04 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0004_alter_blog_fl_number_of_views'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_number', models.IntegerField(default=0, verbose_name='Номер версии продукта')),
                ('version_name', models.CharField(max_length=150, verbose_name='Имя версии продукта')),
                ('indicator', models.BooleanField(default=True, verbose_name='Признак активности продукта')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flowers.flowers', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ['version_name'],
            },
        ),
    ]
