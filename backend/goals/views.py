from rest_framework import viewsets, permissions
from .models import Goal
from .serializers import GoalSerializer

class GoalViewSet(viewsets.ModelViewSet):
    serializer_class = GoalSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only allow authenticated users to access goals

    def get_queryset(self):
        # Only fetch goals for the logged-in user
        return Goal.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically associate the goal with the logged-in user
        serializer.save(user=self.request.user)
