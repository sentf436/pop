from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import Product
from product.serializers import ProductSerializer


class ProductsListView(ListAPIView):
    queryset = Product.objects.only('title')
    serializer_class = ProductSerializer


class ProductsDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CreateProductsView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class UpdateProductsView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer






@api_view(['GET'])
def product(request):
    prod = Product.objects.only('title')
    serializer = ProductSerializer(prod, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def product_detail(request, pk):
    prod = Product.objects.get(id=pk)
    serializer = ProductSerializer(prod, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def create_product(request):
    prod = Product.objects.all()
    serializer = ProductSerializer(prod, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def update_product(request):
    prod = Product.objects.all()
    serializer = ProductSerializer(prod, many=True)
    return Response(serializer.data)


@api_view(['PATCH'])
def update_product_patch(request):
    prod = Product.objects.all()
    serializer = ProductSerializer(prod, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_product(request):
    prod = Product.objects.all()
    serializer = ProductSerializer(prod, many=False)
    return Response(serializer.data)


class ProductListView(ListAPIView):
    queryset = Product.objects.only('title')
    serializer_class = ProductSerializer


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CreateProductView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class UpdateProductView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class DeleteProductView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductSerializer
        elif self.action == 'retrieve':
            return ProductSerializer
        return ProductSerializer
