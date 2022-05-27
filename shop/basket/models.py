from django.db import models
from myauth.models import MyUser
from paintings.models import Painting


class Basket(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)


class ProductToBasketConnection(models.Model):
    product = models.ForeignKey(Painting, on_delete=models.CASCADE)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
