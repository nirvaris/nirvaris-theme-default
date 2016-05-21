import re

from django import template
from django.conf import settings
from django.template.loader import render_to_string

NV_THEME_GALLERY_IMAGES = 'static/gallery/'

if hasattr(settings, 'NV_THEME_GALLERY_IMAGES'):
    if settings.NV_THEME_GALLERY_IMAGES:
        NV_THEME_GALLERY_IMAGES = settings.NV_THEME_GALLERY_IMAGES

register = template.Library()

@register.filter
def vertical_thumbs(imgs):

    images = []

    for img in imgs:
        images.append({
            'tinny': img.tinny,
            'small': img.small,
            'full': img.full,
            'description': img.description,
        })

    c = {}
    c['images'] = images

    return render_to_string('tag-vertical-thumbs.html',c)

@register.filter
def horizontal_thumbs(imgs):

    images = []

    for img in imgs:
        images.append({
            'tinny': img.tinny,
            'small': img.small,
            'full': img.full,
            'description': img.description,
        })

    c = {}
    c['images'] = images

    return render_to_string('tag-horizontal-thumbs.html',c)
