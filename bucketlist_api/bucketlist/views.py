from bucketlist.serializers import BucketlistSerializer, ItemsSerializer
from bucketlist.models import Bucketlist, Item
from rest_framework import viewsets, permissions

# Create your views here.


class BucketlistViewSet(viewsets.ModelViewSet):

    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer


class ItemsViewSet(viewsets.ModelViewSet):

    queryset = Item.objects.all()
    serializer_class = ItemsSerializer
