# from auth_accounts.serializers import UserSerializer
from bucketlist.models import Bucketlist, Item
from rest_framework import serializers


class BucketlistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bucketlist
        fields = '__all__'

    def create(self, validated_data):
        bucketlist_data = validated_data.pop('bucketlist')
        bucketlist = Bucketlist.objects.create(**validated_data)
        Bucketlist.objects.create(bucketlist=bucketlist, **bucketlist_data)
        return bucketlist

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class ItemsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
