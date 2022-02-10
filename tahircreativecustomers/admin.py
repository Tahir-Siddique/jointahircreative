
from django.contrib import admin
from .models import Order, UserRecord,Option
# Register your models here.

admin.site.register(UserRecord)
admin.site.register(Order)
admin.site.register(Option)