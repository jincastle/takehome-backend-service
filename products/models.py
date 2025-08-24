from django.db import models


__all__ = (
    'Tag',
    'Product',
    'ProductOption',
)


class Tag(models.Model):
    """상품 태그 모델"""
    name = models.CharField('태그명', unique=True, max_length=100)

    class Meta:
        db_table = 'tags'
        verbose_name = '태그'
        verbose_name_plural = '태그들'

    def __str__(self):
        return self.name


class Product(models.Model):
    """상품 모델"""
    name = models.CharField('상품명', max_length=100)
    tag_set = models.ManyToManyField(
        Tag, 
        blank=True,
        verbose_name='태그들'
    )

    class Meta:
        db_table = 'products'
        verbose_name = '상품'
        verbose_name_plural = '상품들'

    def __str__(self):
        return self.name


class ProductOption(models.Model):
    """상품 옵션 모델"""
    product = models.ForeignKey(
        Product, 
        verbose_name='상품',
        related_name='option_set', 
        related_query_name='option', 
        on_delete=models.CASCADE
    )
    name = models.CharField('옵션명', max_length=100)
    price = models.IntegerField('가격')

    class Meta:
        db_table = 'product_options'
        verbose_name = '상품 옵션'
        verbose_name_plural = '상품 옵션들'

    def __str__(self):
        return self.name
