from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee_info
from .forms import Employee_infoForm,EmployeeUpdateForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,login,authenticate
# Homepage with login required
@login_required
def homepage(request):
    employees = Employee_info.objects.all()
    return render(request, "homepage.html", {"employees": employees})

# Add employee view with login required
@login_required
def add_employee(request):
    if request.method == "POST":
        form = Employee_infoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("homepage")
        else:
            return render(request, "add_employee.html", {"form": form})
    else:
        form = Employee_infoForm()
    return render(request, "add_employee.html", {"form": form})

# Delete employee with login required
@login_required
def delete_employee_info(request, pk):
    try:
        employee = Employee_info.objects.get(pk=pk)
        employee.delete()
        return redirect("homepage")
    except Employee_info.DoesNotExist:
        return HttpResponse("Employee profile does not exist.")

# Employee profile with login required
@login_required
def profile(request, pk):
    try:
        employee = Employee_info.objects.get(pk=pk)
        return render(request, "employee_profile.html", {"employee": employee})
    except Employee_info.DoesNotExist:
        return HttpResponse("Not found.")

def update(request,pk):
    employee=Employee_info.objects.get(pk=pk)
    if request.method == "POST":
        employee_form=EmployeeUpdateForm(request.POST,instance=employee)
        if employee_form.is_valid():
            employee_form.save()
            return redirect("homepage")
    else:
        employee_form=EmployeeUpdateForm(instance=employee)
    return render(request,"update.html",{"form":employee_form})

def login_view(request):
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect("homepage")
    else:
        form=AuthenticationForm()
    return render(request,'registration/login.html',{"form":form})
    
    
def log_out(request):
    logout(request)
    return redirect('login')

@login_required
def update_page(request):
    employees=Employee_info.objects.all();
    return render (request,"update_page.html",{"employees":employees})