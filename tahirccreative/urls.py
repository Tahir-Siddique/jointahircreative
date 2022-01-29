from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
<<<<<<< HEAD
    path('authenticatecustomer/', include("tahircreativecustomers.urls")),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

=======
    path('admin/', admin.site.urls),
    path('', include("tahircreativecustomers.urls")),
    path('authenticatecustomer/', include("tahircreativecustomers.urls")),
]
>>>>>>> c223336634ebd10d931a007162d3820d9b042639
