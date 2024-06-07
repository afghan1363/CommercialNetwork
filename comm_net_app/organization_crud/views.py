from rest_framework.viewsets import ModelViewSet
from comm_net_app.models import Organization
from comm_net_app.organization_crud.serializers import OrganizationSerializer


class OrganizationView(ModelViewSet):

    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()
    