from django.shortcuts import render, HttpResponse, redirect
from myapp.models import EmployeeDetails
from myapp.forms import EmployeeDetailsForm

def index(self):
    return HttpResponse("hello")

def register(request):
    if request.method == "POST":
        form = EmployeeDetailsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/allemployees')
            except:
                pass
    else:
        form = EmployeeDetailsForm()
    return render(request, 'index.html', {'form':form})

def allemployees(request):
    details = EmployeeDetails.objects.all()
    return render(request, 'allemployees.html', {'details':details})