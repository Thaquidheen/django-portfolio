from django.shortcuts import render
from .models import about,slider,client1
# Create your views here.
def home(request):
    aboutdata=about.objects.all()[0]
    slidedata=slider.objects.all()
    clientdata = client1.objects.all()
    context={
        'about':aboutdata,
        'slider':slidedata,
        'client':clientdata,
    }
    return render(request,'index.html',context)

def aboutus(request):
    return render(request,'about.html')

