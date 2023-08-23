from django.shortcuts import render, redirect

from .forms import CreateGoodsForm
from .models import Goods, Categories



# from django.http import HttpResponse
# Create your views here.
def product_card(request):
    # return HttpResponse('Ноутбук Apple Macbook Air 13" M2 2022 MLXY3')
    context = {
        'product_title': 'Ноутбук Apple Macbook Air 13" M2 2022 MLXY3',
        'product_description': """
                        13.6" 2560 x 1664, 
                        IPS, 60 Гц, 
                        Apple M2, 8 ГБ, SSD 256 ГБ, 
                        видеокарта встроенная, Mac OS, 
                        цвет крышки серебристый, аккумулятор 52.6 Вт·ч""",
        'product_img_url': 'https://content2.onliner.by/catalog/device/header/c7d28e78749461b622b5054454818022.jpeg'
    }

    return render(request, 'goods/product_card.html', context=context)

def all_goods(request):
    goods = Goods.objects.all()
    context = {
        "goods": goods
    }
    return render(request, 'goods/goods_all.html', context=context)




def create_goods(request):
    if request.method == 'POST':
        form = CreateGoodsForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            categoty = form.cleaned_data['categoty']
            img_url = form.cleaned_data['img_url']
            price = form.cleaned_data['price']
            is_active = form.cleaned_data['is_active']
            goods_news = Goods.objects.create(
                name=name,
                description=description,
                category=categoty,
                img_url=img_url,
                price=price,
                is_active=is_active

            )

            return redirect(all_goods)
        context = {"form": form}

    else:
        form = CreateGoodsForm()
        context = {"form": form}

    return render(
        request,
        "goods/create_goods.html",
        context
    )

