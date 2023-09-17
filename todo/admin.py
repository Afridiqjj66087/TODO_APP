from django.contrib import admin
from .models import Task



class Taskadmin(admin.ModelAdmin):
    list_display = ('task','is_completed','created_at','updated_at')
    search_fields = ('tasks',)
# Register your models here.
admin.site.register(Task,Taskadmin)