from django.contrib import admin
from .models import Tower
# Register your models here.
class TowerAdmin(admin.ModelAdmin):
    fields = ['name', 'level', 'pump','updated']
    list_display = ['name','level', 'pump','updated']
    readonly_fields = ['updated']


admin.site.register(Tower,TowerAdmin)