from django.urls import path

from main import views

urlpatterns=[
    path('',views.index,name='index'),
    path('article/<int:pk>',views.article,name='article'),
    path('author/<int:pk>',views.author,name="author"),
    path('create_article',views.create_article,name="createarticle")
]

#get aritcel
#post articel
#get articel/.id
