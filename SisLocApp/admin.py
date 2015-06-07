from django.contrib import admin

# Register your models here.
from .models import Users, Customers, Product, Features

admin.site.register(Users)
admin.site.register(Customers)
admin.site.register(Product)
admin.site.register(Features)
