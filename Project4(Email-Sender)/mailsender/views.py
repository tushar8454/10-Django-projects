from django.shortcuts import render,HttpResponse

from django.core.mail import send_mail
# Create your views here.

def index(request):
    if request.method == "POST":
        sub=request.POST.get('subject')
        msg=request.POST.get('message')
        email=request.POST.get('email')
        print(sub,msg,email)
        send_mail(
            sub,msg,'mail@gmail.com',
            [email]
        )
        return HttpResponse('email send that !')
    
    return render(request,'mailsender/form.html',{})