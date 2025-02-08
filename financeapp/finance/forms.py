from django import forms
from django.forms import DateInput
from .models import Budget, Category, Transaction

class TransactionForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=True)
    date = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=DateInput(attrs={
            'placeholder': 'DD/MM/YYYY',
        })
    )
    class Meta:
        model = Transaction
        fields = ['type', 'amount', 'category', 'date', 'description']

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['category', 'limit', 'start_date', 'end_date']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
