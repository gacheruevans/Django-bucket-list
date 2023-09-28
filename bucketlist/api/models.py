from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Bucketlist(models.Model):
    """
    This class contains the database schema of the  bucket list
    i.e Table and Columns
    """

    title = models.CharField(max_length=125, unique=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='creator')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)


class Item(models.Model):
    """This model represents a single item in our bucket lists."""

    title = models.CharField(max_length=125)
    done = models.BooleanField(default=False)
    bucketlistId = models.ForeignKey(
        Bucketlist, on_delete=models.CASCADE, related_name='bucketlist_id')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
