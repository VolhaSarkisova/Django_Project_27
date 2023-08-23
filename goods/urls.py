from django.urls import path
from goods.views import product_card, all_goods, create_goods

urlpatterns = [
    path('apple/', product_card),
    path('all_goods/', all_goods),
    path('add/', create_goods),
]