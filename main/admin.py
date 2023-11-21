from django.contrib import admin

from main.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Класс CategoryAdmin для отображения," \
    фильтрации и поиска модели Category"""
    list_display = ('title', 'parent')
    list_filter = ('title', 'parent',)
    search_fields = ('parent',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Класс ProductAdmin для отображения," \
    фильтрации и поиска модели Product"""
    list_display = ('title', 'category', 'count', 'price')
    list_filter = ('title', 'category', 'price',)
    search_fields = ('category',)


