from django.views.generic.base import TemplateView
from django.shortcuts import render


# Create your views here.

class HomePageView(TemplateView):
    template_name = "core/base.html"