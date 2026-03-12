from django import forms
from .models import EmployeeFeedback
import re
from datetime import date

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

    # Employee ID validation
    def clean_employee_id(self):
        emp_id = self.cleaned_data['employee_id']

        if not emp_id.startswith("EMP"):
            raise forms.ValidationError("Employee ID must start with 'EMP'")

        return emp_id


    # Phone validation
    def clean_phone(self):
        phone = self.cleaned_data['phone']

        if not re.fullmatch(r'\d{10}', phone):
            raise forms.ValidationError("Phone number must be exactly 10 digits")

        return phone


    # Experience validation
    def clean_experience(self):
        exp = self.cleaned_data['experience']

        if exp < 0:
            raise forms.ValidationError("Experience cannot be negative")

        return exp


    # Joining date validation
    def clean_joining_date(self):
        joining_date = self.cleaned_data['joining_date']

        if joining_date > date.today():
            raise forms.ValidationError("Joining date cannot be in the future")

        return joining_date