from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', include("tahircreativecustomers.urls")),
    path('authenticatecustomer/', include("tahircreativecustomers.urls")),
    path('admin/', admin.site.urls),
]