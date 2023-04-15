
from django.contrib import admin
from django.urls import path
# now here i am include a include
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('main.urls'))
]
