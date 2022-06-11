from rest_framework import serializers
from .models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed


class RegisterSerializer(serializers.ModelSerializer):
    firstName = serializers.CharField(max_length=50)
    lastName = serializers.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['email', 'firstName', 'lastName']

    def validate(self, attrs):
        email = attrs.get('email', '')
        firstName = attrs.get('firstName', '')
        lastName = attrs.get('lastName', '')
        if not email:
            raise serializers.ValidationError('The email should not be null')
        if not firstName:
            raise serializers.ValidationError('The firstName should not be empty')
        if not lastName:
            raise serializers.ValidationError('The lastName should not be empty')
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(max_length=68, min_length=8, write_only=True)
    access_token = serializers.CharField(max_length=555, min_length=8, read_only=True)
    refresh_token = serializers.CharField(max_length=555, min_length=8, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'access_token',
                  'refresh_token']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        user = auth.authenticate(email=email, password=password)
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')

        return {
            'id': user.id,
            'email': user.email,
            'firstName': user.firstName,
            'lastName': user.lastName,
            'profile_image': user.profile_image,
            'access_token': user.tokens()['access'],
            'refresh_token': user.tokens()['refresh']
        }
        return super().validate(attrs)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'firstName', 'lastName', 'profile_image']
