from django.contrib import admin

from category.models import Category
from product.models import Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'piece_price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)
