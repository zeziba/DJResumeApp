"""resumeapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include as dj_include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from upload.views import ImagesView, ImageUploadView
from index.views import HomePageView, AboutPageView, WorkHistoryView, SkillView, FactsFiveWsView, TermsOfServiceView, PrivacyView, EducationView
from contact.views import ContactUsView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('about/', AboutPageView.as_view(), name="about"),
    path("image/", ImageUploadView.as_view(), name="upload"),
    path("images/", ImagesView.as_view(), name="images_display"),
    path("admin/", admin.site.urls, name="admin"),
    path("education/", EducationView.as_view(), name="education"),
    path("work_experience/", WorkHistoryView.as_view(), name="work_experience"),
    path("work_experience/", dj_include("index.urls"), name="work_experience"),
    path("skills/", SkillView.as_view(), name="skills"),
    path("skills/", dj_include("index.urls"), name="skills"),
    path("facts_5_ws/", FactsFiveWsView.as_view(), name="facts_5_ws"),
    path("contact_us/", ContactUsView.as_view(), name="contact_us"),
    path("terms_of_service/", TermsOfServiceView.as_view(), name="terms_of_service"),
    path("privacy/", PrivacyView.as_view(), name="privacy"),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
