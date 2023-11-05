from .import views
from django.urls import path

from Static_Project import settings
from django.conf.urls.static import static

urlpatterns = [
    path('registration',views.register,name = 'registration'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout')
]