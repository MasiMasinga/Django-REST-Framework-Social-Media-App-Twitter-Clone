from rest_framework import serializers
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import get_user_model
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'date_joined',
                  'last_login', 'is_admin', 'is_active', 'is_staff', 'is_superuser', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User.objects.create_user(**validated_data)

        if password is not None:
            user.set_password(password)
            user.save()

        refresh = RefreshToken.for_user(user)
        validated_data['refresh'] = str(refresh)
        validated_data['access'] = str(refresh.access_token)

        return validated_data

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password is not None:
            instance.set_password(password)

        refresh = RefreshToken.for_user(instance)
        validated_data['refresh'] = str(refresh)
        validated_data['access'] = str(refresh.access_token)

        instance.save()
        return validated_data


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token['email'] = user.email

        return token

class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        self.reset_form = PasswordResetForm(data=self.initial_data)
        if not self.reset_form.is_valid():
            raise serializers.ValidationError('Invalid email.')
        return value

    def save(self):
        request = self.context.get('request')
        self.reset_form.save(use_https=request.is_secure(), request=request)


class SetPasswordSerializer(serializers.Serializer):
    token = serializers.CharField()
    uid = serializers.CharField()
    password = serializers.CharField()
    confirm_password = serializers.CharField()

    def validate(self, attrs):
        try:
            uid = urlsafe_base64_decode(attrs.get('uid')).decode()
            user = get_user_model().objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
            raise serializers.ValidationError({'uid': ['Invalid value']})

        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')

        if password != confirm_password:
            raise serializers.ValidationError({"message": "Passwords do not match."})

        data = {
            'new_password1': password,
            'new_password2': confirm_password,
            'token': attrs.get('token'),
            'uid': attrs.get('uid'),
        }

        self.set_password_form = SetPasswordForm(user=user, data=data)

        if not self.set_password_form.is_valid():
            raise serializers.ValidationError(self.set_password_form.errors)
        return attrs
    
    def save(self):
        return self.set_password_form.save()