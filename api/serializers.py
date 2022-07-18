from rest_framework import serializers
from .models import Songs

class SongsSerializer(serializers.ModelSerializer):
 class Meta:
  model = Songs
  fields = ['artist_name', 'duration', 'platform', 'song_title']
  #fields = ('__all__')