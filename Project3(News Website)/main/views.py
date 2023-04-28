from django.shortcuts import render

from main import models

# Create your views here.

def home(request):
    blog=models.News.objects.all()
    context={'blog':blog}
    return render(request,'index.html',context)

def article(request,pk):
    article=models.News.objects.get(pk=pk)
    context={
        'article':article,
    }
    return render(request,'article.html',context)

def cat(request):
    cat=models.Cat.objects.all()
    context={'cat':cat}
    return render(request,'cat.html',context)

def cat_page(request,pk):
    cat_page=models.News.objects.get(pk=pk)
    blogs=models.News.objects.filter(category=cat_page)
    context={'cat_page':cat_page,
             'blogs':blogs}
    return render(request,'cat_page.html',context)

def single_news(request):
    context={}
    return render(request,'single_news.html',context)

def contact(request):
    context={}
    return render(request,'contact.html',context)
