from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Категория')
    description = models.TextField(**NULLABLE, verbose_name='Описание')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'Категория'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Категории'  # Настройка для наименования набора объектов


class Flowers(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    Imag = models.ImageField(upload_to='products/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')
    date_of_creation = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    last_modified_date = models.DateField(auto_now=True, verbose_name='Дата последнего изменения')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name} {self.category} {self.price} {self.date_of_creation}'

    class Meta:
        verbose_name = 'Цветок'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Цветы'  # Настройка для наименования набора объектов
        db_table = 'store_fl_m'
        db_table_comment = 'Магазин цветов'
        ordering = ['name']


class Blog_fl(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    slug = models.CharField(max_length=150, verbose_name='Slug')
    content = models.TextField(**NULLABLE, verbose_name='Содержимое')
    Imag = models.ImageField(upload_to='products/', verbose_name='Превью', **NULLABLE)
    date_of_creation = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    is_publication = models.BooleanField(default=True, verbose_name='Признак публикации')
    number_of_views = models.IntegerField(verbose_name='Количество просмотров', **NULLABLE)

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name} {self.date_of_creation} {self.is_publication} {self.number_of_views}'

    class Meta:
        verbose_name = 'блог'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Блоги'  # Настройка для наименования набора объектов
        db_table = 'blog'
        db_table_comment = 'Блог и комментарии'
        ordering = ['number_of_views']


