from django import forms

from product.models import Category, Product


# class ProductForm(forms.Form):
#     def __init__(self, *args, **kwargs):
#         super(ProductForm, self).__init__()
#
#     name = forms.CharField(max_length=100)
#     description = forms.CharField()
#     price = forms.DecimalField(max_digits=10,
#                                decimal_places=2)
#     category = forms.ModelChoiceField(queryset=Category.objects.all())
#
#     def save(self):
#         data = self.cleaned_data
#         product = Product.objects.create(**data)
#         return product

class ProductForm(forms.ModelForm):
    # TODO: загрузка изображений
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category']