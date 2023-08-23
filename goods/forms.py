from django import forms

from goods.models import Goods, Categories


class CreateGoodsForm(forms.Form):
    class Meta:
        model = Goods
        fields = ['name', 'description', 'categoty']

    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=3000)
    categoty = forms.ModelChoiceField(queryset=Categories.objects.all().order_by('name').filter(('is_active', True),))
    img_url = forms.URLField(max_length=500)
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    is_active = forms.BooleanField()