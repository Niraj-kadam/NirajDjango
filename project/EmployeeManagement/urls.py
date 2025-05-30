from django.urls import path
from . import views

urlpatterns = [
    path('home', views.homepage),
    path('ecom',views.ecom),
    path('delete/<int:id>',views.deleteOrder),
    path('alter/<int:id>',views.alterOrder),
    path('data',views.dataChange),
    path('buy/<int:id>',views.buyProduct),
    path('addToCart/<int:id>',views.addTocart),
    path('cart',views.cartpage)
]