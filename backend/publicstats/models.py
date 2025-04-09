from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class PostcodeInfo(models.Model):
    pcName = models.CharField(max_length=50)
    postcode = models.CharField(max_length=2, unique=True)
    salary = models.IntegerField(validators=[MinValueValidator(0)])
    housePrice = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return self.postcode

class CostLiving(models.Model):
    SIZE = (
        (1, "1"),
        (4, "4"),
    )
    familySize = models.IntegerField(choices=SIZE)
    accom = models.IntegerField(validators=[MinValueValidator(0)])
    util = models.IntegerField(validators=[MinValueValidator(0)])
    food = models.IntegerField(validators=[MinValueValidator(0)])
    transport = models.IntegerField(validators=[MinValueValidator(0)])
    ent = models.IntegerField(validators=[MinValueValidator(0)])
    other = models.IntegerField(validators=[MinValueValidator(0)])
    postcode = models.ForeignKey(PostcodeInfo, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['familySize', 'postcode']

    def __str__(self):
        return f"{self.postcode} Family of {self.familySize}"
    
    def total(self):
        return self.accom + self.util + self.food + self.transport + self.ent + self.other

#>12,570 = 0%
#12,571-50,270 = 20%
#50,271-125,140 = 40%
#<125,140 = 45%
# Create your models here.
