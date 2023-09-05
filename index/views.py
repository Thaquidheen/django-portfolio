from django.shortcuts import render
from .models import about,slider
# Create your views here.
def home(request):
    aboutdata=about.objects.all()[0]
    slidedata=slider.objects.all()
    context={
        'about':aboutdata,
        'slider':slidedata
    }
    return render(request,'index.html',context)

def aboutus(request):
    return render(request,'about.html')

def contactus(request):
    return render(request,'contact.html')