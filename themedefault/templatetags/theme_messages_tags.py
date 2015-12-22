from django import template
from django.template.loader import render_to_string
from django.utils import six
from django.utils.html import mark_safe

import re

register = template.Library()

@register.filter
def messages_style(messages):

    c = {}
    c['messages'] = messages
    return render_to_string('tag-messages-snippet.html',c)
