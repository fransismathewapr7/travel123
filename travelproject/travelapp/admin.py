from django.contrib import admin

from travelapp.models import Place
from . models import People

# Register your models here.
admin.site.register(Place)
admin.site.register(People)

