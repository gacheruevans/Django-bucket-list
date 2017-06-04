from django.db import models
from datetime import datetime


class Base(models.Model):
    """
    Base model for other database tables to inherit
    """
    __abstract__ = True

    id = models.Integer(primary_key=True)
    date_created = models.DateTime(timezone=True, default=datetime.utcnow())
    date_modified = models.DateTime(timezone=True, nullable=True)


class Account(Base):
    """
    This class contains the database schema of the auth_user
    i.e. Table and Columns
    """

    __tablename__ = 'auth_user'

    username = models.String(max_length=128, nullable=False, unique=True)
    # Identification Data: email & password
    email = models.String(max_length=128, nullable=False, unique=True)
    password = models.CharField(max_length=192, unique=False, nullable=False)

    def verify_password(self, password):
        """
        Function to verify the password of a user
        """
        return self.password == password

    def __repr__(self):
        return '<User %r>' % (self.username)
