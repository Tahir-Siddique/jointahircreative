from django.urls import path
from .views import isUserBlocked,error,project_details
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', error,name="error"),
    path('projects/<slug>', project_details,name="details"),
    path('<str:key>', isUserBlocked,name="isUserBlocked"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
