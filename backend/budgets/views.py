from rest_framework import viewsets, permissions
from .models import Budget
from .serializers import BudgetSerializer

class BudgetViewSet(viewsets.ModelViewSet):
    serializer_class = BudgetSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only allow authenticated users to access budgets

    def get_queryset(self):
        # Only fetch budgets for the logged-in user
        return Budget.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically associate the budget with the logged-in user
        serializer.save(user=self.request.user)
