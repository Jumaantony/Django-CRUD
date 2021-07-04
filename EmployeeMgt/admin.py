from django.contrib import admin
from .models import Employee

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
    'ID',
    'Date_of_Employement',
    'Name', 
    'Email', 
    'Phone_Number',
    'Job' 
    )