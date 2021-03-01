from django.contrib.auth.models import User, Group
from rest_framework import serializers

from seen.models import Category, Tag


class CategorySerializer(serializers.ModelSerializer):
    # parent = serializers.PrimaryKeyRelatedField(read_only=True, queryset=)

    class Meta:
        model = Category
        fields = ['id', 'title', 'created_at', 'updated_at', 'parent_id']

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title', 'created_at', 'updated_at']


# TODO 学习DRF 暂时写在这，后续移到其他地方
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']