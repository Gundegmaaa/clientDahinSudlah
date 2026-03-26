from django import forms
from .models import Worker


class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ['branch', 'first_name', 'last_name', 'position', 'salary', 'hired_date']
        widgets = {
            'hired_date': forms.DateInput(attrs={'type': 'date'}),
        }
