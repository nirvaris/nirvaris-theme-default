from django import template
from django.template.loader import render_to_string
from django.utils import six
from django.utils.html import mark_safe

import re

register = template.Library()

@register.filter
def form_style_horizontal(form):

    c = {}
    c['form'] = form
    return render_to_string('tag-form-horizontal-snippet.html',c)

@register.filter
def form_style(form):

    c = {}
    c['form'] = form
    return render_to_string('tag-form-snippet.html',c)

@register.inclusion_tag('tag-form-script.html')
def form_script():

    return {}

@register.filter
def add_css_class(field,css_classes):

    bf = field

    html_filed = six.text_type(bf)

    m = re.search('class="(.*?)"',html_filed)

    if m:
        html_filed = html_filed.replace(m.group(1),(m.group(1)).strip() + ' ' + css_classes)
    else:
        html_filed = html_filed.replace('<input','<input class="%s"' % css_classes)
        html_filed = html_filed.replace('<textarea','<textarea class="%s"' % css_classes)

    return mark_safe(html_filed)

@register.filter
def field_type(field):

    html_filed = six.text_type(field)

    if 'checkbox' in html_filed:
        return 'checkbox'
    if 'textbox' in html_filed:
        return 'textbox'
    if 'textarea' in html_filed:
        return 'textarea'

    return 'textbox'
