from django.contrib import admin
from .models import Songs
# Register your models here.

@admin.register(Songs)
class StudentAdmin(admin.ModelAdmin):
 list_display = ['id', 'artist_name', 'duration', 'platform','song_title']