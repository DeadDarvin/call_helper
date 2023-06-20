from django.db.models import Q
from django.contrib.auth import get_user_model

from typing import Optional


User = get_user_model()


class AuthBackend(object):
    support_object_permissions = True
    support_anonymous_user = True
    support_inactive_user = True

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    def authenticate(self, request, username: str, password: str) -> Optional[User]:
        """ get user model for auth and check password """

        try:
            user = User.objects.get(
                Q(username=username) |
                Q(email=username) |
                Q(phone_number=username)
            )
        except User.DoesNotExist:
            return None

        return user if user.check_password(password) else None
