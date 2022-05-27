from django.contrib import admin

from .models import Basket, ProductToBasketConnection

admin.site.register(Basket)
admin.site.register(ProductToBasketConnection)
