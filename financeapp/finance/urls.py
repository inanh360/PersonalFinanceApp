from django.urls import path
from . import views

urlpatterns = [
    path('', views.front_page, name='front_page'),
    path('test', views.testRef, name='test'),
    path('transactions/', views.transaction_list, name='transaction_list'),
    path('transactions/add/', views.add_transaction, name='add_transaction'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/add/', views.add_category, name='add_category'),
    path('budgets/', views.budget_list, name='budget_list'),
    path('budgets/add/', views.add_budget, name='add_budget'),
    path('budgets/track/', views.budget_tracking, name='budget_tracking'),
    #path('testing/', views.testing, name='transaction_list'),
    path('transactions/<year>/', views.yearly_list, name='transaction_list'),
    path('transactions/<year>/<month>/', views.monthly_list, name='transaction_list'),
    path('transactions/<year>/<month>/<day>', views.daily_list, name='transaction_list'),
]
