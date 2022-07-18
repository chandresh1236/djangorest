from django.db import models

# Create your models here.
class Songs(models.Model):
 artist_name = models.CharField(max_length=100)
 duration = models.IntegerField()
 platform = models.CharField(max_length=100)
 song_title = models.CharField(max_length=100)