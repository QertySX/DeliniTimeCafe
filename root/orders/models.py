from django.db import models
from django.contrib.auth.models import User
from menu.models import Product


class Order(models.Model):
    # Модель замовлення товару у кошику користувача
    title = models.CharField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)


class OrderHistory(models.Model):
        # Модель замовлення товару у кошику користувача
    title = models.CharField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)