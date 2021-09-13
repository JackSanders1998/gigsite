from django.contrib import admin
from .models import Gig, User, Group


class GigAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'start_datetime', 'end_datetime')

class UserAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

class GroupAdmin(admin.ModelAdmin):
    list_display = ('url', 'username', 'email', 'completed')

admin.site.register(Gig, GigAdmin)
