from itertools import chain

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.postgres.search import SearchVector
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DetailView, ListView, CreateView

from .forms import LoginForm, EmployeeModelForm, JobModelForm
from .models import Employee, Job


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
    return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return render(request, 'registration/logout.html')


@login_required
def dash(request):
    job_count = Job.objects.count()
    employee_count = Employee.objects.count()

    return render(request, 'dash.html', {
        'job_count': job_count,
        'employee_count': employee_count,
    })


class EmployeeList(LoginRequiredMixin, ListView):
    model = Employee
    template_name = 'employee-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = EmployeeModelForm()
        return context

    def post(self, request):
        form = EmployeeModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('EmployeeMgt:employeelist')


class EmployeeDetail(LoginRequiredMixin, DetailView):
    model = Employee
    template_name = 'employee_detail.html'


class EditEmployee(LoginRequiredMixin, UpdateView):
    model = Employee
    template_name = 'edit_employee.html'
    template_name_suffix = '_update_form'
    fields = '__all__'
    success_url = reverse_lazy('EmployeeMgt:employeelist')


def delete_employee(request, pk):
    employee = Employee.objects.get(pk=pk)
    employee.delete()
    return redirect('EmployeeMgt:employeelist')


class JobList(LoginRequiredMixin, ListView):
    model = Job
    template_name = 'job-list.html'


class CreateJob(LoginRequiredMixin, CreateView):
    model = Job
    form_class = JobModelForm
    template_name = "add_job.html"
    success_url = reverse_lazy('EmployeeMgt:joblist')


class EditJob(LoginRequiredMixin, UpdateView):
    model = Job
    template_name = 'edit_job.html'
    template_name_suffix = '_update_form'
    fields = '__all__'
    success_url = reverse_lazy('EmployeeMgt:joblist')


def deletejob(request, pk):
    job = Job.objects.get(pk=pk)
    job.delete()
    return redirect('EmployeeMgt:joblist')


def search(request):
    if request.method == 'GET':
        query = request.GET['search_query']
        search_results = Employee.objects.annotate(
            search=SearchVector('Name', 'Email', 'Phone_Number'),
        ).filter(search=query)

        search_results2 = Job.objects.annotate(
            search=SearchVector('name'),
        ).filter(search=query)

        total_result = len(list(chain(search_results, search_results2)))

        context = {
            'search_results': search_results,
            'search_results2': search_results2,
            'total_result': total_result,
        }

        return render(request, 'search.html', context)

"""
# delete view with the confirm delete in a different page
# case this view is used you need to remove the javascript onlick func and add pk=job.pk in the url

class DeleteJob(LoginRequiredMixin, DeleteView):
    model = Job
    template_name = 'job_confirm_delete.html'
    success_url = reverse_lazy('EmployeeMgt:joblist')

# edit view
def editjob(request, pk):
    obj = get_object_or_404(Job, pk=pk)
    
    form = JobModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('EmployeeMgt:joblist')

    context = {'form': form}

    return render(request, 'edit_job.html', context)

# list view
def job_list(request):
    jobs = Job.objects.all()
    context = {'form': JobModelForm(),
               'jobs': jobs, }
    return render(request, 'job-list.html', context)
    
# create view 
def create_job(request):
    if request.method == "POST":
        form = JobModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('EmployeeMgt:joblist')
    else:
        form = JobModelForm()
    return render(request, 'add_job.html', {'form': form})

"""
