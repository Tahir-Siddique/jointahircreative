from django.http import JsonResponse

from .models import UserRecord

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

def error(request):
    return JsonResponse({"error":"Provide a Selling key"})

