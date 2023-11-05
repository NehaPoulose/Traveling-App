from django.urls import path
from .import views

from Static_Project import settings
from django.conf.urls.static import static

urlpatterns = [

    path('',views.display,name = 'Home')
]