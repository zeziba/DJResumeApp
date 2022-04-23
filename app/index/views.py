from typing import Any
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.db import ProgrammingError
from index.models import WorkExperience, Skills, PersonalInfo, FiveWs, FactsForFiveWs, SocialMedia, Education, Projects


class HomePageView(TemplateView):
    template_name = 'index/resume_home.html'

    def get_context_data(self, **kwargs: Any):
        context = super(HomePageView, self).get_context_data(**kwargs)
        try:
            # The following get the first entry in th personal info database, which limits the app to one resume
            context['personal_info'] = PersonalInfo.objects.get(id=1)
        except PersonalInfo.DoesNotExist or ProgrammingError:
            context['personal_info'] = PersonalInfo()
        try:
            context['social_media'] = SocialMedia.objects.all()
        except SocialMedia.DoesNotExist or ProgrammingError:
            context['social_media'] = SocialMedia()

        return context


class AboutPageView(TemplateView):
    template_name = 'index/about.html'

    def get_context_data(self, *args, **kwargs: Any):
        context = super(AboutPageView, self).get_context_data(*args, **kwargs)
        try:
            context['five_ws'] = FiveWs.objects.get(id=1)
        except FiveWs.DoesNotExist:
            context['personal_info'] = FiveWs()
        try:
            context['facts_5_ws'] = FactsForFiveWs.objects.all()
        except FiveWs.DoesNotExist:
            context['facts_5_ws'] = FactsForFiveWs()

        return context


class WorkHistoryView(TemplateView):
    template_name = 'index/workexperience.html'

    def get_context_data(self, *args, **kwargs: Any):
        context = super(WorkHistoryView, self).get_context_data(
            *args, **kwargs)
        context['work_experience'] = WorkExperience.objects.all()

        return context


class EducationView(TemplateView):
    template_name = 'index/education.html'

    def get_context_data(self, *args, **kwargs: Any):
        context = super(EducationView, self).get_context_data(
            *args, **kwargs)
        context['education'] = Education.objects.all()
        context['education_projects'] = Projects.objects.all()

        return context


class SkillView(TemplateView):
    template_name = 'index/skills.html'

    def get_context_data(self, *args, **kwargs: Any):
        context = super(SkillView, self).get_context_data(*args, **kwargs)
        context['skills'] = Skills.objects.all()

        return context


class TermsOfServiceView(TemplateView):
    template_name = 'index/tos.html'


class PrivacyView(TemplateView):
    template_name = 'index/privacy.html'


def work_experience_detail(request, work_id) -> HttpResponse:
    try:
        work_experience = WorkExperience.objects.get(pk=work_id)
    except WorkExperience.DoesNotExist:
        raise Http404("Work experience does not exist.")
    context = {
        "work_experience": work_experience,
    }
    return render(request=request, template_name="index/partials/workexperience.html", context=context)


def skill_detail(request, skill_id) -> HttpResponse:
    try:
        skills = Skills.objects.get(pk=skill_id)
    except Skills.DoesNotExist:
        raise Http404("Work experience does not exist.")
    context = {
        "skills": skills,
    }
    return render(request=request, template_name="index/partials/skill.html", context=context)


def index(request) -> HttpResponse:
    return HttpResponse("Index page")
