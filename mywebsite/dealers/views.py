from django.shortcuts import render
from django.http import *

# Create your views here.

def homedealers(request):

    return render(request,"dealerhome.html")

def dealerreg(request):

    return render(request,"dealerreg.html")

def dealerprocess(request):

    print(request.method)

    dname= request.POST.get("uname")
    age= request.POST.get("age")
    gender= request.POST.get("gender")
    city= request.POST.get("city")

    print(dname , " " , age , " " , gender ,   "  " , city)
    
    return HttpResponse(f" Hi {dname} ! , Welcome to New India Dealership for the City {city} !!")


def regdispform(request):
    return render(request,"regform1.html")


def candprocess(request):
    print(request.method)

    cname = request.POST["uname"]
    cage = request.POST.get("age")
    cgender = request.POST.get("gender")
    ccity = request.POST.get("city")
    cqual = request.POST.get("qual")
    chobby = request.POST.getlist("hobby") #WHENEVER YOU PASS multiple items use getlist
    cmobile = request.POST.get("mobile")
    cbrief = request.POST.get("brief")
   
    print(cname, " " , cage, " " , cgender, " " , ccity, " " , cqual, " " , chobby, " " , cmobile, " " , cbrief)

    context = { "cname" :cname,"cage":cage, "cgender":cgender,"ccity":ccity,"cqual":cqual,"chobby":chobby,"cmobile":cmobile, "cbrief":cbrief }

    return render(request,"candidatedata.html",context )

