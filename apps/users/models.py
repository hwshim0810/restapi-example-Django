from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from utility.validators import username_validator
from utility.models import CreateAtModel


class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        if not email:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(PermissionsMixin, CreateAtModel, AbstractBaseUser):

    ANONYMOUS_MEMBER_ID = 1

    email = models.EmailField(
        unique=True,
        validators=[username_validator()],
        verbose_name=_('이메일'),
    )
    name = models.CharField(
        max_length=20,
        verbose_name=_('이름'),
        blank=True
    )
    job = models.CharField(
        max_length=20,
        verbose_name=_('직업'),
        blank=True
    )
    followers = models.ManyToManyField(
        "self",
        blank=True
    )
    following = models.ManyToManyField(
        "self",
        blank=True
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name=_('관리자'),
    )

    objects = UserManager()
    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = _('유저')
        verbose_name_plural = _('유저 (User)')

    def __str__(self):
        return self.email

    def get_full_name(self):
        return f'{self.id}({self.email})'.strip()

    def get_short_name(self):
        return self.email
