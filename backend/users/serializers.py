from rest_framework import serializers
from .models import User, Profile

# Serializer for the User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'timezone', 'currency']

# Serializer for the Profile model
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'avatar', 'bio']
