from rest_framework.generics import UpdateAPIView, CreateAPIView
from users import serializers


class NewUserAPIView(CreateAPIView):
    serializer_class = serializers.NewUserSerializer

class JoinToOrganization(UpdateAPIView):
    pass


class RegisterWithNewOrganization(CreateAPIView):
    pass



