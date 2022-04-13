from django.urls import path
from . import views

urlpatterns = [
    path('<int:work_id>/', view=views.work_experience_detail, name='work_experience'),
]
