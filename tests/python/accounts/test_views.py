import pytest
import json

from http.client import OK, CREATED, BAD_REQUEST
from knox.models import AuthToken

from accounts.views import (
    UserRegisterView, UserConfirmEmailView, UserLoginView,
    UserEmailConfirmationStatusView
)


@pytest.mark.django_db(transaction=False)
def test_user_register_view(rf, user_data):
    data = {
        'email': user_data.get('email'),
        'first_name': user_data.get('first_name'),
        'last_name': user_data.get('last_name'),
        'password': user_data.get('password')
    }

    request = rf.post(
        '/register/', json.dumps(data), content_type='application/json'
    )

    response = UserRegisterView.as_view()(request)
    assert response.status_code == CREATED


@pytest.mark.django_db(transaction=False)
def test_user_register_view_without_email(rf, user_data):
    data = {
        'email': 'nomail',
        'first_name': user_data.get('first_name'),
        'last_name': user_data.get('last_name'),
        'password': user_data.get('password')
    }

    request = rf.post(
        '/register/', json.dumps(data), content_type='application/json'
    )

    response = UserRegisterView.as_view()(request)
    assert response.status_code == BAD_REQUEST


@pytest.mark.django_db(transaction=False)
def test_user_confirm_email_view(rf, user):
    request = rf.get('/confirm/email/')

    response = UserConfirmEmailView.as_view()(
        request, activation_key=f'{user.activation_key}'
    )
    assert response.status_code == OK


@pytest.mark.django_db(transaction=False)
def test_user_login_view(rf, user, user_data):
    user.set_password(user_data.get('password'))
    user.save()
    request = rf.post(
        '/login/',
        content_type='application/json',
        HTTP_AUTHORIZATION=f'Basic {user_data.get("auth")}'
    )

    response = UserLoginView.as_view()(request)
    assert response.status_code == OK


@pytest.mark.django_db(transaction=False)
def test_user_email_confirmation_status_view(rf, user, user_data):
    user.set_password(user_data.get('password'))
    user.save()
    token = AuthToken.objects.create(user)

    request = rf.get('/status/email/', HTTP_AUTHORIZATION=f'Token {token}')
    request.user = user
    response = UserEmailConfirmationStatusView.as_view()(request)
    assert response.status_code == OK
