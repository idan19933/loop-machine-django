from django.shortcuts import render
from .models import Sound



def home_view(request):
    sounds =  Sound.objects.all()
    return render(request,'home_page.html',{'sounds':sounds})

def home_view2(request):
    sounds =  Sound.objects.all()
    return render(request,'home_page.html',{'sounds':sounds})
