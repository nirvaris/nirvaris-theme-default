from django import template
from django.template import Context
from django.template.loader import render_to_string
from django.utils import six
from django.utils.html import mark_safe

import re

register = template.Library()

@register.filter
def messages_style(messages):
    
    c = Context()
    c['messages'] = messages
    return render_to_string('messages-snippet.html',c)