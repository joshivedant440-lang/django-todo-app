from django.contrib import admin
from .models import Task
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display=("title","completed", "created_at")
    list_filter =("completed",)
    search_fields=("title",)