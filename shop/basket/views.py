from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render

from .models import Basket, ProductToBasketConnection


def CheckoutView(request):
    basket = find_or_create_basket(request.user.id)
    total_price = 0
    for connection in basket.productConnections.all():
        total_price += connection.product.price
    return render(request, template_name="basket/basket_detail.html",
                  context={'basket':basket, 'total_price':total_price})

def AddToBasket(request):
    basket = find_or_create_basket(request.user.id)
    productId = request.GET.get('id')
    connQuery = ProductToBasketConnection.objects.filter(basket_id=basket.id, product_id=productId)
    if len(connQuery) > 0:
        return HttpResponseBadRequest("Product is already in the basket")
    else:
        new_conn = ProductToBasketConnection(basket_id=basket.id, product_id=productId)
        new_conn.save()

    return HttpResponse("OK")

def find_or_create_basket(user_id):
    basketQuery = Basket.objects.filter(pk=user_id)

    if len(basketQuery) == 0:
        new_basket = Basket(user_id=user_id)
        new_basket.save()
        basket = new_basket
    else:
        basket = basketQuery[0]

    return basket

def checkout_apply(request):
    user = request.user
    basket = find_or_create_basket(user.id)
    productConnections = basket.productConnections.all()
    for connection in productConnections:
        if connection.product.isordered:
            return HttpResponseBadRequest("Sorry, but you can't buy " + str(connection.product.name) +
                                          ". It is already gone. :(")
    for connection in productConnections:
        connection.product.isordered = True
        connection.product.save()
        connection.delete()

    return HttpResponse("OK")



def delete_product_from_basket(request):
    user = request.user
    basket = find_or_create_basket(user.id)
    productId = request.GET.get('id')
    connQuery = ProductToBasketConnection.objects.filter(basket_id=basket.id, product_id=productId)
    if len(connQuery) > 0:
        connQuery[0].delete()
        return HttpResponse("OK")
    else:
        return HttpResponseBadRequest("Product isn't in the basket")




