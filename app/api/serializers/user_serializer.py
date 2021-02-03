from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        user = User.objects.create(**validated_data)
        return user

    def update(self, instance, validated_data):
        if validated_data.get('password') != "null":
            instance.password = make_password(validated_data.get('password', instance.password))
        else:
            instance.password = instance.password

        instance.save()
        return instance
