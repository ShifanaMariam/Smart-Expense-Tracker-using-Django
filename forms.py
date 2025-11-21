from django import forms
from .models import Expense
from .utils import predict_category

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['description','amount','date','category','notes']
        widgets = {
            'date': forms.DateInput(attrs={'type':'date'}),
        }

    def save(self, commit=True, user=None):
        instance = super().save(commit=False)
        if not instance.category or instance.category == 'Other':
            instance.category = predict_category(instance.description)
        if user:
            instance.user = user
        if commit:
            instance.save()
        return instance
