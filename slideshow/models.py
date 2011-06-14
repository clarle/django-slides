from django.db import models
import datetime

# Create your models here.

class Slide(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    slideshow = models.ForeignKey('Slideshow')
    image = models.ImageField(upload_to='slideshow', max_length=500, blank=True,null=True)

    def __unicode__(self):
        return self.title

class Slideshow(models.Model):
    name = models.CharField(max_length=50)
    preload = models.BooleanField()
    hover_pause = models.BooleanField()
    crossfade = models.BooleanField()
    big_target = models.BooleanField()
    captions = models.BooleanField()
    arrows = models.BooleanField()
    play = models.IntegerField(blank=True, default=0)
    pause = models.IntegerField(blank=True, default=0)
    pub_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name
