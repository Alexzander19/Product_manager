from django.db import models

# Create your models here.

# Опишите модель Product с полями:
# name — название товара (строка, максимум 200 символов).
# description — описание товара (текстовое поле).
# price — цена товара (десятичное число с двумя знаками после запятой).
# created_at — дата добавления товара.

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name +": " + self.description[:15] + '...'
