from django.db import models
from django.conf import settings

class Account(models.Model):
    ACCOUNT_TYPES = [
        ('BANK', 'Bank Account'),
        ('CREDIT', 'Credit Card'),
        ('CASH', 'Cash Wallet'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=ACCOUNT_TYPES)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    institution = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.type})"
