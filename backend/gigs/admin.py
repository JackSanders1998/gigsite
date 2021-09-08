from django.contrib import admin
from .models import Todo, Question, Gig


class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

class GigAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'start_datetime', 'end_datetime')

# Register your models here.

admin.site.register(Gig, GigAdmin)
