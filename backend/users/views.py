from rest_framework import viewsets, permissions
from .models import User, Profile
from .serializers import UserSerializer, ProfileSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

# View for handling User data (although User data will mostly be managed by Django auth)
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Allow users to access only their own data
        return User.objects.filter(id=self.request.user.id)

# View for handling Profile data
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only fetch the profile of the logged-in user
        return Profile.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically associate the profile with the logged-in user
        serializer.save(user=self.request.user)
