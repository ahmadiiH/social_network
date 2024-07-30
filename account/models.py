from django.db import models
from django.conf import settings


class Country(models.Model):
    name = models.CharField(max_length=50)
    abb = models.CharField(max_length=5)
    is_active = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time =   models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'country'
        verbose_name_plural = 'countries'
        db_table = 'countries'


class Profile(models.Model):
    user = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.BigIntegerField(blank=True, null=True , unique=True)
    country = models.ForeignKey(to=Country, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True)

class Device(models.Model):
    DEVICE_WEB = 1
    DEVICE_IOS = 2
    DEVICE_ANDROID = 3
    DEVICE_PC = 4
    DEVICE_TYPE_CHOICES = (
        (DEVICE_WEB ,  'web'),
    (DEVICE_IOS ,  'ios'),
    (DEVICE_ANDROID ,  'android'),
    (DEVICE_PC ,  'pc'),

    )
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,related_name='devices', on_delete=models.CASCADE)
    device_uuid = models.UUIDField('device uuid', null=True)
    last_login = models.DateTimeField('last login date', null=True)
    device_type = models.PositiveIntegerField(choices=DEVICE_TYPE_CHOICES,default=DEVICE_WEB)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time =   models.DateTimeField(auto_now=True)