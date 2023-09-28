from rest_framework import serializers
from .models import User, Bucketlist, Item


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'created_at')

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user


class BucketlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bucketlist
        fields = ('id', 'title', 'created_by')

    def create(self, validated_data):
        bucketlist_data = validated_data.pop('bucketlist')
        bucketlist = Bucketlist.objects.create(**validated_data)
        Bucketlist.objects.create(bucketlist=bucketlist, **bucketlist_data)
        return Bucketlist

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance


class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
