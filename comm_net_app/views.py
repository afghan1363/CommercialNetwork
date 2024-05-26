from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from comm_net_app import serializers, models


class OrganizationCreateAPIView(CreateAPIView):
    serializer_class = serializers.OrganizationsCreateSerializer


class OrganizationListAPIView(ListAPIView):
    queryset = models.Organization.objects.all()
    serializer_class = serializers.OrganizationSerializer


class OrganizationRetrieveAPIView(RetrieveAPIView):
    queryset = models.Organization.objects.all()
    serializer_class = serializers.OrganizationSerializer


class OrganizationUpdateAPIView(UpdateAPIView):
    queryset = models.Organization.objects.all()
    serializer_class = serializers.OrganizationSerializer


class OrganizationDestroyAPIView(DestroyAPIView):
    queryset = models.Organization.objects.all()


class BuyProduct(UpdateAPIView):
    pass
