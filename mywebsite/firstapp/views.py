from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# Function Based Views

def index(request):
    return HttpResponse(" Welcome to Django !")


def mypage(request):
    return HttpResponse(" <h1> This is the Second Page   !</h1>")


def test(request):
    return HttpResponse(" <Center><h2> This is For Testing Purposes   !</h2>")

def htmltest(request):
    return render(request,"index.html")

def regform(request):
    return render(request,"inputdata.html")

def getregdata(request):
    uname = request.GET.get("uname")
    city = request.GET.get("ucity")
    print(uname)
    print(city)
    # return HttpResponse(f" <h3> Hi { uname } ! Welcome ! You are from {   city } !!!</h1>",content_type='text/html')
    return render(request, "welcome.html", {"uname": uname, "city": city})