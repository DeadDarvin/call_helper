from django.contrib.auth.base_user import BaseUserManager
from rest_framework.exceptions import ParseError


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user_in_db(self, email: str = None,
                           password: str = None, username: str = None, phone_number: str = None, **extra_fields):
        """ DB layer method for creation user """
        if not (email or phone_number):
            raise ParseError("Укажите email или телефон")

        if email:
            email = self.normalize_email(email)

        if not username:
            if email:
                username = email.split("@")[0]
            else:
                username = phone_number

        user = self.model(username=username, **extra_fields)
        user.email = email
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email: str = None,
                         password: str = None, username: str = None, phone_number: str = None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        return self._create_user_in_db(email, password, username, phone_number, **extra_fields)

    def create_user(self, email: str = None,
                    password: str = None, username: str = None, phone_number: str = None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_active', True)

        return self._create_user_in_db(email, password, username, phone_number, **extra_fields)
