from django.urls import path
from . import views

urlpatterns = [
    path('', views.postcodeList, name='all_house'),
    path('<id>', views.yearsForHouse, name='yearly_house'),
]
