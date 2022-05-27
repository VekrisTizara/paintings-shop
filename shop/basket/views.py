from django.shortcuts import render
from .models import Basket
from django.views.generic import ListView

class CheckoutView(ListView):
    model = Basket

