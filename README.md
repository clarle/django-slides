# Django Slides

A Django application that makes it easy to add, edit, and deploy slideshows using the excellent [Slides.js](https://github.com/nathansearles/slides/) jQuery plugin by [Nathan Searles](https://github.com/nathansearles).

## Installation

1. Download and place the 'slideshow' folder somewhere  on your `PYTHONPATH`. 
2. Add `slideshow` to your `INSTALLED_APPS` under `settings.py`.
3. To use a slideshow in another Django application, you can refer to the `slideshow` object as `slideshow.Slideshow` in your Django models.
4. If you're not extending `base.html`, make sure you have jQuery 1.4.2+ and Slides 1.1.7+ in your templates somewhere. Use `{% load slideshow_tags %}` in whatever template you wish to use a slideshow in. 

## Usage

Create a slideshow in the Django admin panel by selecting desired effects and customizing slides as needed. Slides can be created with images and captions, or just pure text (formatted as HTML). 

Use the slideshow in a template (after properly loading it) with:

    `{% place_slides Slideshow %}`

Where `Slideshow` is some Slideshow object. 

## Customization

Buttons, frames, and pagination can be changed inside the `static/img` folder and CSS can be changed inside the `static/css` folder.

## To-do List

* Custom pagination
* Better admin panel

## License

Django Slides is licensed under the [Apache license](http://www.apache.org/licenses/LICENSE-2.0).
