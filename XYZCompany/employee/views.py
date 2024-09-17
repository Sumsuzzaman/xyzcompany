from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmployeeForm
from .models import Employee
from django.contrib.auth.decorators import login_required

# View for listing all employees (Homepage)
def home(request):
    employees = Employee.objects.all()
    return render(request, 'employee/home.html', {'employees': employees})

# View for adding a new employee
@login_required
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EmployeeForm()
    return render(request, 'employee/add_employee.html', {'form': form})

# View for updating employee
@login_required
def update_employee(request, id):  # Accept 'id' as the argument
    employee = get_object_or_404(Employee, id=id)  # Get the employee using the id
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()  # Save the updated employee information
            return redirect('home')  # Redirect to the homepage after successful update
    else:
        form = EmployeeForm(instance=employee)  # Pre-fill form with the employee's data
    
    return render(request, 'employee/update_employee.html', {'form': form})

# View for deleting an employee
@login_required
def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        employee.delete()
        return redirect('home')
    return render(request, 'employee/delete_employee.html', {'employee': employee})


