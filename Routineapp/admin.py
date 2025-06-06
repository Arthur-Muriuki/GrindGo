from django.contrib import admin
from .models import Routine

@admin.register(Routine)
class RoutineAdmin(admin.ModelAdmin):
    list_display = ('title', 'day', 'time', 'user')

