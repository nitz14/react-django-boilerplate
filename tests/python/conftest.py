import pytest
import responses

import django
from django.conf import settings

from accounts.models import User

django.setup()


@pytest.fixture(scope="module")
@pytest.fixture
def user_data():
    return {
        'last_name': 'Doe',
        'first_name': 'John',
        'email': 'John.Doe@example.com',
        'password': 'passJohn1',
        'auth': 'Sm9obi5Eb2VAZXhhbXBsZS5jb206cGFzc0pvaG4x'
    }


@pytest.fixture(scope="module")
def superuser(user_data):
    superuser, _ = User.objects.get_or_create(
        email=user_data['email'],
        first_name=user_data['first_name'],
        last_name=user_data['last_name'],
        is_staff=True,
        is_active=True,
        is_superuser=True,
    )
    return superuser


@pytest.fixture(scope="module")
def user(user_data):
    user, _ = User.objects.get_or_create(
        password=user_data.get('password'),
        last_name=user_data.get('last_name'),
        first_name=user_data.get('first_name'),
        email=user_data.get('email'),
        is_staff=False,
        is_active=True,
        is_superuser=False,
    )
    return user
