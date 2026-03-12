from django import forms
from .models import EmployeeFeedback

class EmployeeFeedbackForm(forms.ModelForm):

    class Meta:
        model = EmployeeFeedback
        fields = "__all__"

        widgets = {
            'employee_name': forms.TextInput(attrs={'class':'form-control'}),
            'employee_id': forms.TextInput(attrs={'class':'form-control'}),
            'department': forms.Select(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
            'joining_date': forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'experience': forms.NumberInput(attrs={'class':'form-control'}),
            'feedback': forms.Textarea(attrs={'class':'form-control'}),
            'recommendations': forms.Textarea(attrs={'class':'form-control'}),
        }