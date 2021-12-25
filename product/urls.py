from django.urls import path

from product.views import *

urlpatterns = [
    path('', ProductListView.as_view(), name='products-list'),
    path('<int:pk>/', ProductDetailsView.as_view(), name='product-details'),
    path('create/', CreateProductView.as_view(), name='create-product'),
    path('update/<int:pk>/', UpdateProductView.as_view(), name='update-product'),
    path('delete/<int:pk>/', DeleteProductView.as_view(), name='delete-product'),
    path('search/', SearchResultsView.as_view(), name='search')
]