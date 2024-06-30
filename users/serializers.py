from rest_framework.serializers import ModelSerializer, IntegerField, CharField, BooleanField
from users.models import User
from comm_net_app.organization_crud.serializers import OrganizationSerializer



class NewUserSerializer(ModelSerializer):
    password = CharField(min_length=20, write_only=True)
    phone = CharField(allow_null=True)
    city = CharField(max_length=200, allow_null=True)
    # organization = models.ForeignKey(to=Organization, on_delete=models.CASCADE, verbose_name=_('Organization'),
    #                                  related_name='employee', **NULLABLE)
    moderator = BooleanField(default=False)


    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            phone=validated_data['phone'],
            city=validated_data['city'],
            moderator=validated_data['moderator']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = '__all__'


class NewUserWithOrgSerializer(ModelSerializer):
    organization = OrganizationSerializer()

    def create(self, validated_data):
        org = validated_data.pop('organization')
        user = User.objects.create(
            email=validated_data['email'],
            phone=validated_data['phone'],
            city=validated_data['city'],
            moderator=validated_data['moderator']
        )
        
        user.set_password(validated_data['password'])
        user.save()
        return user


    class Meta:
        model = User
        fields = '__all__'
