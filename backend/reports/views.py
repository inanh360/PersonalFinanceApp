from rest_framework import viewsets, permissions
from .models import Report
from .serializers import ReportSerializer

class ReportViewSet(viewsets.ModelViewSet):
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only allow authenticated users to access reports

    def get_queryset(self):
        # Only fetch reports for the logged-in user
        return Report.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically associate the report with the logged-in user
        serializer.save(user=self.request.user)
