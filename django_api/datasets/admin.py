from django.contrib import admin
from .models import DataSet

class DataAdmin(admin.ModelAdmin):
    pass

admin.site.register(DataSet,DataAdmin)