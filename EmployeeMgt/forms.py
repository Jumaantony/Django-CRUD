from django import forms
from .models import Employee, Job


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class EmployeeModelForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('ID', 'Date_of_Employement', 'Name', 'Email', 'Phone_Number', 'Job')


class JobModelForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
