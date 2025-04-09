from django.shortcuts import render
from .models import *
from utils import *

#>12,570 = 0%
#12,571-50,270 = 20%
#50,271-125,140 = 40%
#<125,140 = 45%

def postcodeList(request):
    postcodes = PostcodeInfo.objects.all()
    return 0

def yearsForHouse(request, id):
    postcode = PostcodeInfo.objects.get(id=id)
    time = timeForHouse(postcode)
    return 0
    
def yearlyCost(postcode, size):
    return (CostLiving.objects.get(postcode=postcode, familySize=size).total()) * 12

def timeForHouse(postcode):
    avgSalary = postcode.salary
    avgHouse = postcode.housePrice
    avgPostNat = nationalInsurance(avgSalary)
    avgPostTax = postTaxSal(avgPostNat)
    avgCost1 = yearlyCost(postcode, 1)
    avgCost4 = yearlyCost(postcode, 4)
    return [avgHouse/(avgPostTax-avgCost1), avgHouse/(avgPostTax-avgCost4)]
# Create your views here.
