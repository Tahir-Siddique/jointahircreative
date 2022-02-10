from django.urls import path
from .views import isUserBlocked,project_details,landing
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', landing,name="details"),
    path('projects/<slug>', project_details,name="details"),
    path('validate/<str:key>', isUserBlocked,name="isUserBlocked"),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
