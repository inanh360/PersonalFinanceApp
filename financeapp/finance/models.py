from django.db import models
from django.contrib.auth.models import User

class FinanceUser(models.Model):
    username = models.CharField(max_length=512, unique=True)
    password = models.CharField(max_length=512)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    display_name = models.CharField(
        max_length=512,
    )

    def save(self, *args, **kwargs):
        if self.user is None:
            if User.objects.filter(username=self.username).exists():
                user = User.objects.get(username=self.username)
            else:
                user = User.objects.create_user(username=self.username, password=self.password)
            self.user = user
        super().save(*args, **kwargs)

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Months(models.Model):
    MONTH_CHOICES = [
        (1, 'January'),
        (2, 'February'),
        (3, 'March'),
        (4, 'April'),
        (5, 'May'),
        (6, 'June'),
        (7, 'July'),
        (8, 'August'),
        (9, 'September'),
        (10, 'October'),
        (11, 'November'),
        (12, 'December'),
    ]

    month = models.IntegerField(choices=MONTH_CHOICES)

    def __str__(self):
        return f"Month: {self.get_month_display()}"


class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('income', 'Income'),
        ('expense', 'Expense'),
    )

    type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    #month = models.ForeignKey(Months, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type} - {self.amount} - {self.date}"

class Budget(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    limit = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.category} - {self.limit}"
    
class UserPostInfo(models.Model):
    name = models.CharField(max_length=52)
    postcode = models.ForeignKey("publicstats.PostcodeInfo", on_delete=models.CASCADE)

class Salary(models.Model):
    TYPE = (
        ('1', 'daily'),
        ('2', 'weekly'),
        ('3', 'bi-weekly'),
        ('4', 'monthly'),
        ('5', 'yearly'),
    )

    name = models.CharField(max_length=52)
    amount = models.IntegerField()
    salary_type = models.IntegerField(choices=TYPE)
    user = models.ForeignKey(FinanceUser, on_delete=models.CASCADE)
