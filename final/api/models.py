from __future__ import unicode_literals

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    avatar = models.ImageField(
        upload_to='images/user/',
        null=True,
        blank=True,
    )
    date_of_birth = models.DateField(null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    @property
    def is_staff(self):
        return self.is_superuser


class BookJournalBase(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=128)
    price = models.FloatField(default=0.0)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')


class Book(BookJournalBase):
    num_pages = models.IntegerField()
    genre = models.CharField(max_length=128)


class Journal(BookJournalBase):
    TYPES = [
        ('B', 'Bullet'),
        ('F', 'Food'),
        ('T', 'Travel'),
        ('S', 'Sport'),
    ]
    type = models.CharField(choices=TYPES, default='B', max_length=128)
    publisher = models.CharField(max_length=123)
