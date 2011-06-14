from slideshow.models import Slide, Slideshow
from django.contrib import admin

class SlideInline(admin.StackedInline):
    model = Slide

class SlideshowAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                   {'fields': ['name']}),
        ('Effects', {'fields': [('preload', 
                                'hover_pause',
                                'crossfade',
                                'big_target',
                                'arrows',
                                'captions',
                                )]}),
        ('Speed', {'fields': [('play', 'pause')]}),
    ]
    inlines = [SlideInline]
    list_display = ['name', 'pub_date']
    list_filter = ['pub_date']
    search_fields = ['name']

admin.site.register(Slideshow, SlideshowAdmin)
