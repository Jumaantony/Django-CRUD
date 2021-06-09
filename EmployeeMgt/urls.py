from django.urls import path, include
from . import views
app_name = 'EmployeeMgt'

urlpatterns = [
    path('', views.index, name='index'),
    path('dash/', views.dash, name='dash'),
    path('employeelist/', views.employeelist, name='employeelist'),
    path('joblist/', views.joblist, name='joblist')
]