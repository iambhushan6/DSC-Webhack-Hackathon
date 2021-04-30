from django.contrib import admin
from main import models
from .models import Vac_center,Citizen
# Register your models here.

admin.site.register(Vac_center)
admin.site.register(Citizen)
