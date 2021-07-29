from django.urls import path
from . import views
from .views import JobList, CreateJob, EditJob, EmployeeList, EmployeeDetail, EditEmployee  # CreateEmployee

app_name = 'EmployeeMgt'

urlpatterns = [
    path('', views.user_login, name='user_login'),

    path('logout/', views.logout_view, name='logout_view'),

    path('dash/', views.dash, name='dash'),

    path('employeelist/', EmployeeList.as_view(), name='employeelist'),

    path('employee_detail/<pk>/', EmployeeDetail.as_view(), name='employee_detail'),

    path('delete_employee/<pk>/', views.delete_employee, name='delete_employee'),

    path('edit_employee/<pk>/', EditEmployee.as_view(), name='edit_employee'),

    path('joblist/', JobList.as_view(), name='joblist'),
    # path('joblist/', views.job_list, name='joblist'),

    path('create_job/', CreateJob.as_view(), name='create_job'),
    # path('create_job/', views.create_job, name='create_job'),

    path('edit_job/<pk>/', EditJob.as_view(), name='edit_job'),
    # path('edit_job/<pk>/', views.editjob, name='edit_job'),

    # path('delete_job/<pk>/', DeleteJob.as_view(), name='delete_job'),
    path('delete_job/<pk>/', views.deletejob, name='delete_job')
]
