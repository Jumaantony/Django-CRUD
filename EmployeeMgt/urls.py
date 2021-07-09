from django.urls import path
from . import views

app_name = 'EmployeeMgt'

urlpatterns = [
    path('', views.user_login, name='user_login'),

    path('logout/', views.logout_view, name='logout_view'),

    path('dash/', views.dash, name='dash'),

    path('employeelist/', views.employeelist, name='employeelist'),

    path('joblist/', views.joblist, name='joblist'),

    # path('employee_detail/', views.EmployeeDetailView.as_view(), name='employee_detail'),

]
