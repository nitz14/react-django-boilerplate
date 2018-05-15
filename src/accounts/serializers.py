from rest_framework import serializers

from .models import User
from utils import validate_email as email_is_valid


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class UserRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = (
            'id', 'email', 'first_name', 'last_name', 'password'
        )

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate_email(self, value):
        if not email_is_valid(value):
            raise serializers.ValidationError(
                'Please use a different email address provider.'
            )

        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                'Email already in use, please use a different email address.'
            )

        return value
