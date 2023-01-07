from django.contrib import admin
from .models import Item, Category, Restaurant, Address

# Register your models here.

admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Restaurant)
admin.site.register(Address)


