from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _

from .views import (
    UserLoginView, UserRegisterView, UserConfirmEmailView,
    UserEmailConfirmationStatusView
)

urlpatterns = [
    url(_(r'^register/$'), UserRegisterView.as_view(), name='register'),
    url(_(r'^login/$'), UserLoginView.as_view(), name='login'),
    url(
        _(r'^confirm/email/(?P<activation_key>.*)/$'),
        UserConfirmEmailView.as_view(),
        name='confirm_email'
    ),
    url(
        _(r'^status/email/$'),
        UserEmailConfirmationStatusView.as_view(),
        name='status'
    ),
]
