from django.contrib import admin
from .models import Employee, Job


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


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'date'
    )
