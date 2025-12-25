from rest_framework import serializers
from accounts.models import User
from django.core import exceptions
from django.contrib.auth.password_validation import validate_password

class RegistrationsSerializers(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=250, write_only=True)


    class Meta:
        model = User
        fields = ['email', 'password', 'password1']

    # Check if password and password1 match 
    def validate(self, attrs):
        if attrs.get('password') != attrs.get('password1'):
            raise serializers.ValidationError(
                {'details': 'password dosnt match'}
            )
        try:
            validate_password(attrs.get('password'))
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({'password':list(e.messages)})

        return super().validate(attrs)
    

    # Create user without password 1
    def create(self, validated_data):
        validated_data.pop('password1', None)
        return super().create(**validated_data)
