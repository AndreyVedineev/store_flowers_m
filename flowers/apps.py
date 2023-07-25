from django.apps import AppConfig


class FlowersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'flowers'
    verbose_name = 'Цветы'


class Blog_flConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog_fl'
    verbose_name = 'Блог'
