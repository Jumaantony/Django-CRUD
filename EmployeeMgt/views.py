from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required


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
                    return HttpResponse('Authenticated Successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('invalid Login')
    else:
            form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def dash(request):
    return render(request, 'dash.html', {})

def employeelist(request):
    return render(request, 'employee-list.html', {})


def joblist(request):
    return render(request, 'job-list.html', {})