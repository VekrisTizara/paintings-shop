"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

import myauth.views as myauth

import paintings.views as painting_views
import basket.views as basket_views
from shop.settings import DEBUG, MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    path('', painting_views.index, name='index'),

    path('products/', painting_views.PaintingListView.as_view(), name='painting_list'),
    path('painting/detail/<int:pk>/', painting_views.PaintingDetailView.as_view(), name='painting_detail'),

    path('admin/', admin.site.urls),

    path('register/', myauth.MyUserCreateView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),


    path('checkout/', basket_views.CheckoutView, name='checkout'),
    path('addToBasket/', basket_views.AddToBasket, name='addToBasket'),
    path('applyCheckout/', basket_views.checkout_apply, name='applyCheckout'),
    path('removeFromBasket/', basket_views.delete_product_from_basket, name='removeFromBasket')
]+static(MEDIA_URL, document_root=MEDIA_ROOT)

if DEBUG:
    urlpatterns += path('__debug__/', include('debug_toolbar.urls')),