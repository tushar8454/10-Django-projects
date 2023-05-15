from django.shortcuts import render,redirect

from .models import Employees,Car

from main import models

# Create your views here.
def index(request):
    emp=models.Employees.objects.all()
    context={"emp":emp}
    return render(request,'index.html',context)

def add(request):
    context={}
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        
        emp=Employees(
            name = name,
            email = email,
            address = address,
            phone = phone,
        )
        emp.save()
        return redirect('index')

    return render(request,'index.html',context)


def edit(request):
    
    emp=models.Employees.objects.all()
    context={"emp":emp}
    return render(request,'index.html',context)

def update(request,id):
    if request.method == "POST":
        name=request.POST.get("name"),
        email=request.POST.get("email"),
        address=request.POST.get("address"),
        phone=request.POST.get("phone"),
        
        emp=Employees(
            id = id,
            name = name,
            email = email,
            address = address,
            phone = phone,
        ) 
        emp.save()
        return redirect('index')



    return redirect(request,'index.html')

def delete(request,id):
    emp=models.Employees.objects.filter(id=id).delete()
    context={
        'emp':emp
    }
    return redirect('index')