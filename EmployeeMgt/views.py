from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def dash(request):
    return render(request, 'dash.html', {})

def employeelist(request):
    return render(request, 'employee-list.html', {})


def joblist(request):
    return render(request, 'job-list.html', {})