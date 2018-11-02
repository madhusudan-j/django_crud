from django import forms
from myapp.models import EmployeeDetails

class EmployeeDetailsForm(forms.ModelForm):
    class Meta:
        model = EmployeeDetails
        fields = "__all__"