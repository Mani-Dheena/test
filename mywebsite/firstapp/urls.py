from django.urls import path 
from . import views 

urlpatterns=[
    path("",views.index,name="index"),
    path("secpage",views.mypage,name="secpage"),
    path("about",views.test,name="about"),
    path("main",views.htmltest,name="main"),
    path("register",views.regform,name="register"),
    path("regout",views.getregdata,name="regout"),
    
]