from MyBlog.settings import TEMPLATES
from django.urls import path
from django.urls import path,include    
from . import views
from django.views.generic import TemplateView   

#app_name = "users"
urlpatterns = [
    path("accounts/",include("django.contrib.auth.urls")),
    path("register/",views.register,name = "register"),
    path("profile/",views.profile,name="profile")
    ]