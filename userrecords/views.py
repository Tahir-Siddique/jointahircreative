from django.http import JsonResponse
from django.shortcuts import render

from userrecords.models import UserRecord

# Create your views here.

def isUserBlocked(request,key):
    isBlocked = UserRecord.objects.get(Selling_Key=key).Is_Blocked
    return JsonResponse({"isBlocked":isBlocked})
def error(request):
    return JsonResponse({"error":"Provide a Primary key"})
