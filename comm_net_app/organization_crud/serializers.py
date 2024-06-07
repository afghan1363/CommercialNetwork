from rest_framework.serializers import ModelSerializer, SerializerMethodField
from comm_net_app.models import Organization


class OrganizationSerializer(ModelSerializer):
    is_supplier = SerializerMethodField()
    is_distributor = SerializerMethodField()
    debt = SerializerMethodField()

    def get_is_supplier(self, obj) -> str | None:
        if hasattr(obj, 'Organization'):
            return "Является поставщиком"
        else:
            return "Ничего не производит"
    

    def get_is_distributor(self, obj) -> str | None:
        if obj.supplier:
            return "Является покупателем"
        else:
            return "Не является диллером"
        
    def get_debt(self, obj):
        # debt_list = obj.
        return "Under construction"
        

    class Meta:
        model = Organization
        fields = '__all__'
