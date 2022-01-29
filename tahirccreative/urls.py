from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("tahircreativecustomers.urls")),
    path('authenticatecustomer/', include("tahircreativecustomers.urls")),
]