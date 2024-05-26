from rest_framework.serializers import ModelSerializer
from comm_net_app import models


class OrganizationsCreateSerializer(ModelSerializer):
    class Meta:
        model = models.Organization
        fields = ('id', 'title', 'email', 'country', 'city', 'street', 'building_number',)


class OrganizationSerializer(ModelSerializer):
    # is_supplier =
    # is_distributor =
    class Meta:
        model = models.Organization
        fields = '__all__'


class OrganizationWithSupplierSerializer(ModelSerializer):
    supplier = OrganizationSerializer(source='organization', read_only=True)

    class Meta:
        model = models.Organization
        fields = '__all__'


class FirstLevelOrgSerializer(ModelSerializer):
    supplier = OrganizationWithSupplierSerializer(source='organization', read_only=True)

    class Meta:
        model = models.Organization
        fields = '__all__'


class SetSupplierSerializer(ModelSerializer):
    class Meta:
        model = models.Organization
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'
