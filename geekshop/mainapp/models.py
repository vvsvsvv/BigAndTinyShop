from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='имя', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):

    GENDER_CHOICES = (
        (0, 'унисекс'),
        (1, 'мужской'),
        (2, 'женский')
    )

    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='имя продукта', max_length=128)
    image = models.ImageField(upload_to='products_images', blank=True)
    description = models.TextField(verbose_name='описание продукта', blank=True)
    sex = models.SmallIntegerField(verbose_name='пол', default=0, choices=GENDER_CHOICES)
    price = models.DecimalField(verbose_name='цена продукта', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)

    def __str__(self):
        return f'{self.name} ({self.category.name})'
