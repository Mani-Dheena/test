from django.shortcuts import render
from django.http import *
from . models import Books
from decimal import Decimal
# Create your views here.


def index(request):

    return HttpResponse("<center><h1> THIS IS MY CUSTOMERS APP </H1>")


def homemain(request):
    return render(request,"homepage.html")

#Displays custreg.html
def regpage(request):
    return render(request,"custreg.html")

#Logic for receiving custreg form data 
def regprocess(request):
    unam = request.GET.get("uname")
    yrs = request.GET.get("age")
    gnd = request.GET.get("gender")
    cty = request.GET.get("city")
  
    print(unam, " " , yrs , " " , gnd , " " , cty )
  
    return HttpResponse(f"<h2>Hi { unam }, Welcome to New India Company. You are { yrs }, Gender { gnd } , { cty } ! Thank You </h2>")

#Displays the Input getting form
def facdisppage(request):
    return render(request,"inpnumber.html")

#Gets the data from the factorial input page and processes it
def calculate(request):
    num = int(request.GET.get("facnum"))
    fact = 1

    for i in range(1,num+1):
        fact = fact * i

    print(" Result : " , fact )

    return HttpResponse(f"<h3> Factorial = { fact } </h3>")

def displaybookadd(request):
    return render(request,"bookreg.html")

#Logic for receiving custreg form data 
def bookprocess(request):
    bname = request.GET.get("bname")
    pages = request.GET.get("pages")
    price = request.GET.get("price")
    author = request.GET.get("author")
    
    pr = Decimal(price)
    print(bname, " " , pages , " " , price , " " , author )
  
    Books.objects.create(title=bname, pages=pages, price=pr,author=author,)
    
    return HttpResponse(f"<h2>Hi { bname }, Welcome to New India Company. You are { pages }, Gender { pr } , { author } ! Thank You </h2>")
