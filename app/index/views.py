from ast import Dict
from ctypes.wintypes import HINSTANCE
import imp
from multiprocessing import context
from typing import Any
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.db import models
from index.models import WorkExperience

class HomePageView(TemplateView):
    template_name = 'home.html'
    
class AboutPageView(TemplateView):
    template_name = 'about.html'
    
class WorkHistoryView(TemplateView):
    template_name = 'index/workexperience.html'
    
    def get_context_data(self, *args, **kwargs: Any):
        context =  super(WorkHistoryView, self).get_context_data(*args, **kwargs)
        context['work_experience'] = WorkExperience.objects.all()
        
        return context
    
def work_experience_detail(request, work_id) -> HttpResponse:
    try:
        work_experience = WorkExperience.objects.get(pk=work_id)
    except WorkExperience.DoesNotExist:
        raise Http404("Work experience does not exist.")
    context = {
        "work_experience": work_experience,
    }
    return render(request=request, template_name="index/partials/workexperience.html", context=context)

def index(request) -> HttpResponse:
    return HttpResponse("Index page")
