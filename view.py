from django.shortcuts import render
from result.models import *

def home(request):
    if request.method=="POST":
        a=request.POST['name']
        b=request.POST['phone']
        c=request.POST['email']
        d=request.POST['degree']
        e=request.POST['course'] 
        en=Enquiry(name=a,phone=b,email=c,degree=d,course=e)
        en.save()
    return render(request,'home.html')

def interview(request):
    return render(request,'interview.html')

def login(request):
    return render(request,"login.html")
    

def placement1(request):
    placed=Placement.objects.all()
    return render(request,'placement.html',{'placed':placed})
    # return render(request,'placement.html')

