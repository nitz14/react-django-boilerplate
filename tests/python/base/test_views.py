import pytest

from http.client import OK, UNAUTHORIZED
from knox.models import AuthToken

from base.views import ProtectedDataView


@pytest.mark.django_db(transaction=False)
def test_protected_data_view(rf, user, user_data):
    user.set_password(user_data.get('password'))
    user.save()
    token = AuthToken.objects.create(user)

    request = rf.get('/protected_data/', HTTP_AUTHORIZATION=f'Token {token}')
    request.user = user
    response = ProtectedDataView.as_view()(request)
    assert response.status_code == OK


@pytest.mark.django_db(transaction=False)
def test_protected_data_view_without_token(rf, user, user_data):
    user.set_password(user_data.get('password'))
    user.save()

    request = rf.get('/protected_data/')
    request.user = user
    response = ProtectedDataView.as_view()(request)
    assert response.status_code == UNAUTHORIZED
