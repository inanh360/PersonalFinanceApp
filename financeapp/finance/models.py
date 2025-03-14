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

class Transaction(models.Model):
    name = models.CharField(max_length=52)
    amount = models.IntegerField()
    user = models.ForeignKey(FinanceUser, on_delete=models.CASCADE)