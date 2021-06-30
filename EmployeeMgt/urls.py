from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .views import AddEmployeeView

app_name = 'EmployeeMgt'

urlpatterns = [
    # path('', views.user_login, name='user_login'),

    path('', auth_views.LoginView.as_view(), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('dash/', views.dash, name='dash'),

    path('employeelist/', views.employeelist, name='employeelist'),

    path('add_employee/', AddEmployeeView.as_view(), name='add_employee'),

    path('joblist/', views.joblist, name='joblist')
]
