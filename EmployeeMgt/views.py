from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, EmployeeModelForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from .models import Employee
from bootstrap_modal_forms.generic import BSModalCreateView


# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'dash.html', {})
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('invalid Login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return render(request, 'account/login.html')


@login_required
def dash(request):
    return render(request, 'dash.html', {})


@login_required
def employeelist(request):
    return render(request, 'employee-list.html', {})


class AddEmployeeView(LoginRequiredMixin, BSModalCreateView):
    template_name = 'add_employee.html'
    form_class = EmployeeModelForm
    success_message = 'Employee Added Successfully'
    success_url = reverse_lazy('employeelist')


@login_required
def joblist(request):
    return render(request, 'job-list.html', {})
