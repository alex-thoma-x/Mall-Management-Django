from django.urls import path
from.import views
from django.contrib.auth import views as auth_views

app_name='home'

urlpatterns = [
    path("",views.home,name='home'),
    path("login/",views.homelogin,name='login')
   ]