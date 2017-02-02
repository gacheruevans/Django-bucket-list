from django.db import models
from django.contrib.auth.models import User
from auth_accounts.models import Base


class Bucketlist(Base):
    """
    This class contains the database schema of the Bucketlist
    i.e. Table and Columns
    """

    name = models.CharField(max_length=128, unique=True)
    created_by = models.ForeignKey(User, related_name='creator')

    def __str__(self):
        return '<Bucketlist %r>' % (self.name)

    class Meta:
        ordering = ('name',)


class Item(Base):
    """
    This class contains the database schema of the Items
    i.e. Table and Columns
    """

    name = models.CharField(max_length=128)
    done = models.BooleanField(default=False)
    bucketlist_id = models.ForeignKey(Bucketlist, related_name='bucketlist_id')

    def __str__(self):
        return '<Item %r>' % (self.name)

    class Meta:
        ordering = ('name',)
