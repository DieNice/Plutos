from rest_framework import serializers
from .models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    fullname = serializers.CharField()
    login = serializers.CharField()
    password = serializers.CharField()
    mail = serializers.EmailField()
    phone = serializers.CharField()
    avatar = serializers.CharField()

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.fullname = validated_data.get('fullname', instance.fullname)
        instance.login = validated_data.get('login', instance.login)
        instance.password = validated_data.get('password', instance.password)
        instance.mail = validated_data.get('mail', instance.mail)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.avatar = validated_data.get('avatar', instance.phone)
        instance.save()
        return instance
