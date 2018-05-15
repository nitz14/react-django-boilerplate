import pytest

from accounts.models import User

from accounts.serializers import (
    UserSerializer, UserRegistrationSerializer
)


@pytest.fixture()
def users_key():
    return ['first_name', 'last_name', 'email']


@pytest.fixture()
def users_reg_key():
    return ['email', 'first_name', 'last_name', 'password']


@pytest.mark.django_db(transaction=False)
def test_user_serializer(user, users_key, user_data):
    serializer = UserSerializer(instance=user)
    data = serializer.data
    assert set(data.keys()) == set(users_key)
    for key in users_key:
        assert data[key] == user_data[key]


@pytest.mark.django_db(transaction=False)
def test_user_registration_serializer(user_data, users_reg_key):
    serializer = UserRegistrationSerializer(instance=user_data)
    data = serializer.data
    assert set(data.keys()) == set(users_reg_key)
    for key in users_reg_key:
        assert data[key] == user_data[key]
