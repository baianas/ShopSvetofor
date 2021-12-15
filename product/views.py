from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView

from product.forms import ProductForm
from product.models import Product, Category


# CRUD(Create, Retrieve, Update, Delete)
# TODO: реализовать CRUD
# TODO: авторизация
# TODO: реализовать проверку прав пользователя



class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'product/products_list.html'
    context_object_name = 'products'


class ProductDetailsView(DetailView):
    queryset = Product.objects.all()
    template_name = 'product/product_details.html'
    context_object_name = 'product'


# TODO: реализовать при помощи функции
class CreateProductView(CreateView):
    queryset = Product.objects.all()
    template_name = 'product/create_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('products-list')



# MVC(Model-View-Controller)
#
# Model           (models)
# View            (template)
# Controller      (view)



# request  -->  Controller
# response <-------|
#
#   View          Controller    <---->   Model  <--->    Data Base
#             /        \
#            /          \
# request ->             -> response