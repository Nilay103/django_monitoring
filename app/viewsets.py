from rest_framework import viewsets, filters
from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from customs.pagination import CustomPagination
# from silk.profiling.profiler import silk_profile


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    pagination_class = CustomPagination


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    pagination_class = CustomPagination
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['customer_name', 'order_date']
    search_fields = ['customer_name']

    # @silk_profile(name='OrderViewSet-list')  # Provide a name for the profile
    # def list(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)

    # @silk_profile(name='OrderViewSet-retrieve')  # Provide a name for the profile
    # def retrieve(self, request, *args, **kwargs):
    #     return super().retrieve(request, *args, **kwargs)
