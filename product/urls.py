
from django.urls import path

from product.views import *

urlpatterns = [
    path('func/product/', product),
    path('func/detail/product/<int:pk>/', product_detail),
    path('func/create/product/', create_product),
    path('func/update/product/', update_product),
    path('func/patch/product/', update_product_patch),
    path('func/delete/product/', delete_product),

    path('product/', ProductListView.as_view()),
    path('product/detail/<int:pk>/', ProductDetailView.as_view()),
    path('product/create/', CreateProductView.as_view()),
    path('product/update/', UpdateProductView.as_view()),
    path('product/delete/', DeleteProductView.as_view()),

    path('prod/', ProductViewSet.as_view({'get': 'list',
                                          'post': 'create'})),
    path('prod/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve',
                                                   'put': 'update',
                                                   'patch': 'partial_update',
                                                   'delete': 'destroy'})),

    path('prods/', ProductsListView.as_view()),
    path('prods/details/<int:pk>/', ProductsDetailView.as_view()),
    path('prods/create/', CreateProductsView.as_view()),
    path('prods/update/', UpdateProductsView.as_view()),
    ]
