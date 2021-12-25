from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from order.views import ActivateOrderView
from product.views import ProductListView, ProductDetailsView, CreateProductView, UpdateProductView, DeleteProductView, \
    IndexPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexPageView.as_view(), name='index'),
    path('account/', include('account.urls')),
    path('cart/', include('order.urls')),
    path('products/', include('product.urls')),
    path('order/activate/<str:activation_code>/', ActivateOrderView.as_view())


    # path('home/', include('product.urls')),
    # path('order/', include('order.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
