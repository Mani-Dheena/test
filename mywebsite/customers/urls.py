from django.urls import path 

from . import views 

urlpatterns=[
    path("",views.index,name="index"),
    path("home",views.homemain,name="home"),
    path("customer",views.regpage,name="customer"), #url for display custreg.html
    path("cprocess",views.regprocess,name="cprocess"), #url for getting data from custreg & process
    path("factorial",views.facdisppage,name="factorial"),
    path("faccalc",views.calculate,name="faccalc"),
    path("bookshome",views.displaybookadd,name="bookshome"), #url for display custreg.html
    path("addbooks",views.bookprocess,name="addbooks"), #url for display custreg.html

]