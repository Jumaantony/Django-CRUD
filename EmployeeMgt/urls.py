from django.urls import path
from . import views
from .views import JobList, CreateJob, EditJob

app_name = 'EmployeeMgt'

urlpatterns = [
    path('', views.user_login, name='user_login'),

    path('logout/', views.logout_view, name='logout_view'),

    path('dash/', views.dash, name='dash'),

    path('employeelist/', views.employeelist, name='employeelist'),

    path('edit_employee/', views.EditEmployee.as_view(), name='edit_employee'),

    path('joblist/', JobList.as_view(), name='joblist'),
    # path('joblist/', views.job_list, name='joblist'),

    path('create_job/', CreateJob.as_view(), name='create_job'),
    # path('create_job/', views.create_job, name='create_job'),

    path('edit_job/<pk>/', EditJob.as_view(), name='edit_job'),
    # path('edit_job/<pk>/', views.editjob, name='edit_job'),

    # path('delete_job/<pk>/', DeleteJob.as_view(), name='delete_job'),
    path('delete_job/<pk>/', views.deletejob, name='delete_job')
]
