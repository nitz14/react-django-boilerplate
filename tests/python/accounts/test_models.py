import pytest
import datetime

from django.conf import settings
from django.utils import timezone

from accounts.models import User


@pytest.mark.django_db(transaction=False)
def test_user_save(user, user_data):
    assert str(
        user
    ) == f'{user.id} - {user.full_name}'
    assert user.is_superuser is False
    assert user.is_active is True
    assert user.is_staff is False
    assert user.full_name == 'John Doe'
    assert user.first_name == user_data['first_name']


@pytest.mark.django_db(transaction=False)
def test_superuser_save(superuser, user_data):
    assert superuser.is_superuser is True
    assert superuser.is_active is True
    assert superuser.is_staff is True
    assert superuser.full_name == 'John Doe'
    assert superuser.first_name == user_data['first_name']


@pytest.mark.django_db(transaction=False)
def test_user_confirm_email_with_confirmed_email(user):
    user.confirmed_email = True
    user.save()
    assert user.confirm_email() is False


@pytest.mark.django_db(transaction=False)
def test_user_confirm_email(user):
    assert user.confirm_email() is False


@pytest.mark.django_db(transaction=False)
def test_user_confirm_email_with_activation_expired(user):
    user.date_joined = timezone.now(
    ) - datetime.timedelta(days=settings.ACCOUNT_ACTIVATION_DAYS)
    user.save()
    assert user.confirm_email() is False
