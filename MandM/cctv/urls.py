from django.urls import path
from.import views
from home import views as v
from django.contrib.auth import views as auth_views

app_name='cctv'

urlpatterns = [
    path("",views.home,name='home'),
    # path("signup",views.signup,name="signup"),
    path("login",v.homelogin,name='login'),
    path("logout",views.logout,name='logout'),
    path("add_camera",views.add_camera,name='add_camera'),
    path("full/<int:id>",views.full,name='full'),
    path("delete/<int:id>",views.destroy,name='destroy'),
    path("change_password",views.change_password,name='change_password'),  # This is change pasword,
    path('scookie', views.setcookie),
    path("searchposts",views.searchposts,name='searchposts'),
    path("control",views.control,name='control')






]