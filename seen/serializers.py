from django.contrib.auth.models import User, Group
from rest_framework import serializers


# TODO 学习DRF 暂时写在这，后续移到其他地方
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']