import json, pdb, re

from django import template
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import mark_safe

NV_THEME_TITLE = 'Nirvaris Default Theme'

if hasattr(settings, 'NV_THEME_TITLE'):
    if settings.NV_THEME_TITLE:
        NV_THEME_TITLE = settings.NV_THEME_TITLE

NV_THEME_MICRO_DATA = {
    '@context': 'http://schema.org'
}

if hasattr(settings, 'NV_THEME_MICRO_DATA'):
    if settings.NV_THEME_MICRO_DATA:
        NV_THEME_MICRO_DATA = settings.NV_THEME_MICRO_DATA

NV_THEME_META_DATA = [
    {
        'name': 'description',
        'content': 'This is a Nirvaris Default Theme'
    },
    {
        'name': 'keywords',
        'content': 'django, theme app, nirvaris'
    },
    {
        'name': 'author',
        'content': 'Nirvaris'
    },
    {
        'property': 'og:type',
        'content': 'article'
    },
]

if hasattr(settings, 'NV_THEME_META_DATA'):
    if settings.NV_THEME_META_DATA:
        NV_THEME_META_DATA = settings.NV_THEME_META_DATA

register = template.Library()

@register.simple_tag()
def theme_title(title):
    result = ''
    if NV_THEME_TITLE and NV_THEME_TITLE != '':
        result = NV_THEME_TITLE
    if title and title != '':
        if result != '':
            result += ' - ' + title
        else:
            result = title

    return result


@register.inclusion_tag('tag-micro-data.html')
def micro_data():
    c = {}
    c['theme_micro_data'] = mark_safe(json.dumps(NV_THEME_MICRO_DATA))
    return c

@register.inclusion_tag('tag-meta-data.html')
def meta_data(locals):
    c = {}
    #pdb.set_trace()
    tags =[]
    for tag in NV_THEME_META_DATA:
        if 'name' in tag and _check_locals(locals, tag, 'name'):
            continue
        if 'property' in tag and _check_locals(locals, tag, 'property'):
            continue

        tags.append(tag)

    tags.extend(locals)

    c['meta_data'] = tags
    return c

def _check_locals(locals, tag, k):
    for l in locals:
        if k in l and tag[k]==l[k]:
            return True
    return False
