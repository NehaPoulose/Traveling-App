from django.shortcuts import render
from .models import fastservices
from .models import  teammembers


# Create your views here.
def display(request):
    object = fastservices.objects.all()
    object1 = teammembers.objects.all()
    return render(request,'index.html',{'result':object,'result1':object1})





