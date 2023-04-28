from main import views

from django.urls import path

urlpatterns = [
   path('',views.home,name='home'),
   path('article/<int:pk>',views.article,name='article'),

   path('cat',views.cat,name='cat'),
   path('cat_page/<int:pk>/',views.cat_page,name='cat_page'),

   # path('single_news',views.single_news,name='single_news'),
   # path('contact',views.contact,name='contact'),
  
   

]
