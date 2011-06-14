from django import template
from slideshow.models import Slideshow

register = template.Library()

@register.inclusion_tag('slideshow/slides.html')
def place_slides(show):
    slides = show.slide_set.all()
    captions = show.captions
    arrows = show.arrows
    params = {'play': show.play, 
              'pause': show.pause,
              'preload': show.preload,
              'hoverPause': show.hover_pause,
              'crossfade': show.crossfade,
              'bigTarget': show.big_target,
             }
    filter_params = dict((k,str(v).lower) for k,v in params.iteritems() if v)

    return {'slides': slides, 'captions': captions, 'arrows': arrows, 'params': filter_params}
