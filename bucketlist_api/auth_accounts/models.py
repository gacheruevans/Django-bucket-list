from django.db import models
from django.utils import timezone


class Base(models.Model):
    """
    Base model for other database tables to inherit
    """
    
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
    	__abstract__ = True
