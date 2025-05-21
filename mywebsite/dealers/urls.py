from django.urls import path 

from . import views 

urlpatterns=[
    path("",views.homedealers,name="home"),
    path("dealreg",views.dealerreg,name="dealreg"),
    path("dealprocess",views.dealerprocess,name="dealprocess"),
    path("candreg",views.regdispform,name="candreg"),
    path("canddisplay",views.candprocess,name="canddisplay"),

]