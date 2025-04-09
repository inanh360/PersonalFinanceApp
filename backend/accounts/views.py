from rest_framework import viewsets, permissions
from .models import Account
from .serializers import AccountSerializer

class AccountViewSet(viewsets.ModelViewSet):
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]  # Ensure user is authenticated

    def get_queryset(self):
        return Account.objects.filter(user=self.request.user)  # Only fetch accounts for the logged-in user

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Automatically assign the user to the account
