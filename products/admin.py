from django.contrib import admin
from .models import Tag, Product, ProductOption


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """태그 관리자"""
    list_display = ['name']
    search_fields = ['name']
    ordering = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """상품 관리자"""
    list_display = ['name', 'get_tags', 'get_options_count']
    search_fields = ['name']
    filter_horizontal = ['tag_set']
    
    def get_tags(self, obj):
        """태그 목록을 문자열로 반환"""
        return ', '.join([tag.name for tag in obj.tag_set.all()])
    get_tags.short_description = '태그들'
    
    def get_options_count(self, obj):
        """옵션 개수 반환"""
        return obj.option_set.count()
    get_options_count.short_description = '옵션 개수'


@admin.register(ProductOption)
class ProductOptionAdmin(admin.ModelAdmin):
    """상품 옵션 관리자"""
    list_display = ['product', 'name', 'price']
    list_filter = ['product']
    search_fields = ['name', 'product__name']
    ordering = ['product', 'name']
