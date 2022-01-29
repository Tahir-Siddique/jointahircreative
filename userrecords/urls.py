from django.urls import path
from .views import isUserBlocked,error

urlpatterns = [
    path('', error,name="error"),
    path('<str:key>', isUserBlocked,name="isUserBlocked"),
]
