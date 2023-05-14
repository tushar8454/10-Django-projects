from django.shortcuts import render
from . import models
from django.db.models import Q
# Create your views here.
def index(request):
    if 'q' in request.GET:
        q=request.GET['q']
        # data=models.Data.objects.filter(first_name__icontains=q)
        multiple_q=Q(Q(first_name__icontains=q) | Q(last_name__icontains=q))
        data=models.Data.objects.filter(multiple_q)

    else:
        data=models.Data.objects.all()
    
    context={
        'data':data
    }
    return render(request,'index.html',context)