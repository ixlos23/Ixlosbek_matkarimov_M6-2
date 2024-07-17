from django.contrib import admin
from django.contrib.admin import StackedInline

from apps.models import Product, Category, Specification, ProductImage

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = 'slug',


class ProductImageAdmin(StackedInline):
    model = ProductImage


class SpecifictionAdmin(StackedInline):
    model = Specification


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = ProductImageAdmin, SpecifictionAdmin
    exclude = 'slug',

# @admin.register(Specification)
# class SpecificationAdmin(admin.ModelAdmin):
#     pass
