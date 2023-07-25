from django.contrib import admin

from flowers.models import Category, Flowers, Blog_fl


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    # list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Flowers)
class FlowersAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'date_of_creation', 'last_modified_date', 'Imag')
    list_filter = ('category',)
    search_fields = ('name',)


@admin.register(Blog_fl)
class Blog_flAdmin(admin.ModelAdmin):
    last_display = ('name', 'date_of_creation', 'is_publication', 'number_of_views',)
    last_filter = ('is_publication',)
    search_fields = ('name',)
