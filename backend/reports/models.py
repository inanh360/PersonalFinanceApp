from django.db import models
from django.conf import settings

class Report(models.Model):
    REPORT_TYPES = [
        ('MONTHLY', 'Monthly Summary'),
        ('CATEGORY', 'Spending by Category'),
        ('INCOME_VS_EXPENSE', 'Income vs Expense'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    report_type = models.CharField(max_length=30, choices=REPORT_TYPES)
    generated_at = models.DateTimeField(auto_now_add=True)
    data = models.JSONField()

    def __str__(self):
        return f"{self.report_type} - {self.generated_at.strftime('%Y-%m-%d')}"
