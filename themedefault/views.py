
from django.contrib import messages
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext as _
from django.views.generic import TemplateView
from django.views.generic.base import View


class HomeView(TemplateView):
    template_name = "theme-home.html"