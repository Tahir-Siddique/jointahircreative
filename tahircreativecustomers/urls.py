from django.urls import path
from .views import isUserBlocked,error,project_details

urlpatterns = [
    path('', error,name="error"),
    path('projects/<slug>', project_details,name="details"),
    path('<str:key>', isUserBlocked,name="isUserBlocked"),
]
