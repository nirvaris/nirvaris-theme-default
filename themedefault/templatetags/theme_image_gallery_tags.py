import re

from django import template
from django.template import Context
from django.template.loader import render_to_string


register = template.Library()

@register.filter
def horizontal_thumbs(imgs):
    
    images = []
    
    for img in imgs:
        images.append({
            'tinny': _naming(img.file,'tinny'),
            'small': _naming(img.file,'small'),
            'full': _naming(img.file,'full'),
            'description': img.description,                                    
        })

    c = Context()
    c['images'] = images
    return render_to_string('horizontal-thumbs-tag.html',c)

    
def _naming(img_file_name,name):
    ext = img_file_name.split('.')[-1]
    return img_file_name.replace('.' + ext, '_' + name + '.' + ext)