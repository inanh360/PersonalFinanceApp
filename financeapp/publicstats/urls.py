from django.urls import path
from . import views

urlpatterns = [
    path('general/', views.postcodeList, name='all_house'),
    path('general/<id>', views.yearsForHouse, name='yearly_house'),
]
