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
            'tinny': _naming(img.file_name,'tinny'),
            'small': _naming(img.file_name,'small'),
            'full': _naming(img.file_name,'full'),
            'description': img.description,
        })

    c = {}
    c['images'] = images
    c['gallery_images'] = NV_THEME_GALLERY_IMAGES
    return render_to_string('tag-vertical-thumbs.html',c)

@register.filter
def horizontal_thumbs(imgs):

    images = []

    for img in imgs:
        images.append({
            'tinny': _naming(img.file_name,'tinny'),
            'small': _naming(img.file_name,'small'),
            'full': _naming(img.file_name,'full'),
            'description': img.description,
        })

    c = {}
    c['images'] = images
    c['gallery_images'] = NV_THEME_GALLERY_IMAGES
    return render_to_string('tag-horizontal-thumbs.html',c)


def _naming(img_file_name,name):
    ext = img_file_name.split('.')[-1]
    return img_file_name.replace('.' + ext, '_' + name + '.' + ext)
