from django.db import models
from authapp.models import User
from mainapp.models import Product
from django.conf import settings


class Basket(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE) Первая версия
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для пользователя {self.user} | Продукт {self.product}'

    def total_sum(self):
        return self.quantity * self.product.price
