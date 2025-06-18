from django.shortcuts import render

from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = 'index.html'

class ServicesPage(TemplateView):
    template_name = 'services.html'


class NewsPage(TemplateView):
    template_name = 'news.html'

class FacultiesPage(TemplateView):
    template_name = 'faculties.html'

