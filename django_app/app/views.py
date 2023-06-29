<<<<<<< HEAD
from django.shortcuts import render

# Create your views here.
=======
from django.shortcuts import render,redirect, HttpResponse

# Create your views here.

def toIndex(request):

    return redirect("homepage")


def homepage(request):
    
    # return render(request, 'homepage.html')
    return HttpResponse('<h1 style="color:red;">hello, Welcome to my youtube chanel</h1>')

def about(request):
    
    return HttpResponse("hello, WElcome to my youtube chanel")

def contact(request):
    
    return HttpResponse("hello, WElcome to my youtube chanel")
>>>>>>> 26f8e4740ad362fdf4f7bdcfb5780e6163ba60be
