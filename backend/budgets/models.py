from django.db import models
from django.conf import settings
from transactions.models import Category

class Budget(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    month = models.DateField(help_text="First day of the month (e.g., 2025-04-01)")

    def __str__(self):
        return f"{self.category.name} - {self.month.strftime('%B %Y')}"
