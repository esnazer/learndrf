from django.contrib import admin

# Register your models here.
from .models import Categorial, Product

admin.site.register(Categorial)
admin.site.register(Product)