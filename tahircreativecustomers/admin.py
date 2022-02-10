
from django.contrib import admin
from .models import Order, UserRecord,Options
# Register your models here.

admin.site.register(UserRecord)
admin.site.register(Order)
admin.site.register(Options)