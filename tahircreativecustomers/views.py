from contextlib import nullcontext
from django.http import JsonResponse
from django.shortcuts import render

from .models import Order, UserRecord

# Create your views here.

def isUserBlocked(request,key):
    status = UserRecord.objects.filter(Selling_Key=key).all()
    isBlocked = None
    if(status.count() != 0):
        isBlocked = UserRecord.objects.get(Selling_Key=key).Is_Blocked
    return JsonResponse({

            "success" : status.count(),
            "isBlocked":isBlocked
        })
def landing(request):
    return render(request,"tahircreativecustomers/landing.html",{})
def project_details(request,slug):
    details = Order.objects.filter(slug=slug).first()
    return render(request,"tahircreativecustomers/details.html",{

            "details" : details
        })

def error(request):
    return JsonResponse({"error":"Provide a Selling key"})

