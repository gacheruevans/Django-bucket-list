from django.db import models
from bucketlist.auth.models import Base


class Bucketlist(Base):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=128, blank=True, default='')
    created_by = models.ForeignKey('auth.Account', related_name='bucketlist')

    class Meta:
        ordering = ('created',)


class Item(Base):
    name = models.CharField(max_length=128, blank=True, default='')
    done = models.BooleanField(null=True, blank=True, default='')
    created_by = models.ForeignKey(
        'bucketlist.Bucketlist', related_name='bucketlist')

    class Meta:
        ordering = ('created',)
