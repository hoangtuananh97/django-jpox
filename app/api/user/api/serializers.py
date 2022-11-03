from rest_framework import serializers

from api.user.models import User


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        pass


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def validate(self, attrs):
        return attrs

    def update(self, instance, validated_data):
        pass


class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
