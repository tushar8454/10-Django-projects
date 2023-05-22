from django.shortcuts import render

#view is importing because i made a classes
from django.views import View
from .models import *
from . import models
from .form import *
# this module is used for showing alert or succesfull message show in your templates
from django.contrib import messages

# this is function based view
# def home(request):
#  return render(request, 'app/home.html')

class ProductView(View):
 def get(self,request):
  topwears=Product.objects.filter(category='TW')
  bottomwears=Product.objects.filter(category='BW')
  mobiles=Product.objects.filter(category='M')
  context={
           'topwears':topwears,
           'bottomwears':bottomwears,
           'mobiles':mobiles}
  
  return render(request, 'app/home.html',context)

# def product_detail(request):
#  return render(request, 'app/productdetail.html')
class ProductDetailView(View):
 def get(self,request,pk):
  Any=Product.objects.all()
  product=Product.objects.get(pk=pk)
  context={'product':product,
           'Any':Any}
  return render(request, 'app/productdetail.html',context)

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

# def change_password(request):
#  return render(request, 'app/changepassword.html')

def mobile(request,data=None):
 if data == None:
  mobiles=Product.objects.filter(category='M')
#  elif data == 'mi' or data == 'poco': OR
 elif data != None:
  mobiles=Product.objects.filter(category='M').filter(brand=data)
 elif data == 'below':
  mobiles=Product.objects.filter(category='M').filter(discount_price__lt=900)
 elif data == 'above':
  mobiles=Product.objects.filter(category='M').filter(selling_price__gt=1000)
  
 context={'mobiles':mobiles}
 return render(request, 'app/mobile.html',context)

# def login(request):
#  return render(request, 'app/login.html')

# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')
class customerregistrationView(View):
 def get(self,request):
  form=CustomerRegisterationForm()
  context={'form':form}
  return render(request,'app/customerregistration.html',context)
 def post(self,request):
  form=CustomerRegisterationForm(request.POST)
  if form.is_valid():
   messages.success(request,'congratualation!! Registered Succesfully')
   form.save()
  context={'form':form}
  return render(request,'app/customerregistration.html',context)

def checkout(request):
 return render(request, 'app/checkout.html')
