from django.shortcuts import render, get_object_or_404

# Create your views here.
from main import models
from django.http import Http404


def index(request):
    #  latest_articles=models.Article.objects.all()[:10]
    latest_articles=models.Article.objects.all().order_by('-createdAt')[:10]

    context={
        "latest_articles":latest_articles,
    }
    return render(request,'main/index.html',context)

def article(request,pk):
    # try:
    #     article=models.Article.objects.get(pk = pk)
    # except:
    #     raise Http404()
                #    or
    article=get_object_or_404(models.Article,pk = pk)        
    context={"article":article}
    return render(request,'main/article.html',context)


def author(request,pk):
    author=get_object_or_404(models.Author,pk=pk)
    context={
        "author":author,
    }

    return render(request,'main/author.html',context)


def create_article(request):
    authors=models.Author.objects.all()
    context={
        "authors":authors
    }

    # print(request.POST)
    if request.method == "POST":
        article_data ={
        "title":request.POST['title'],
        "content":request.POST['content'],
        }
        article=models.Article.objects.create(**article_data)
        author=models.Author.objects.filter(pk=request.POST['author'])
        article.authors.set(author)
        context["success"]=True
    
#    - **article_data=like - title=request.POST["title"]
    
    return render(request,'main/createarticle.html',context)
