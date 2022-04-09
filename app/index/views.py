from ctypes.wintypes import HINSTANCE
import imp
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'
    
class AboutPageView(TemplateView):
    template_name = 'about.html'

def index(request):
    return HttpResponse("Index page")
