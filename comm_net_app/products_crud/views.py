from rest_framework.viewsets import ModelViewSet
from comm_net_app.models import Product, Organization
from comm_net_app.products_crud.serializers import ProductSerializer
from rest_framework.generics import ListAPIView


class ProductAPIView(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


    def perform_create(self, serializer):
        # return super().perform_create(serializer)
        manufacturer_pk = self.kwargs.get('org_pk')
        manufacturer = Organization.objects.get(pk=manufacturer_pk)
        new_product = serializer.save()
        new_product.manufacturer = manufacturer
        new_product.save()


    def list(self, request, *args, **kwargs):
        manufacturer_pk = self.kwargs.get('org_pk')
        queryset = Product.objects.filter(manufacturer_pk=manufacturer_pk)
        serializer = self.get_serializer(queryset, many=True)
        return self.get_paginated_response(self.paginate_queryset(serializer.data))
    

class All_ProductAPIView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
