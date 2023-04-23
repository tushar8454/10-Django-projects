from main import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('add',views.add,name='add'),
    path('edit',views.edit,name='edit'),
    path('update/<str:id>',views.update,name='update'),
    path('delete/<str:id>',views.delete,name='delete'),

]
