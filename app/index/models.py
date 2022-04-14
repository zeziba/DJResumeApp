from distutils.text_file import TextFile
from django.db import models

class WorkExperience(models.Model):
    company_name = models.CharField(max_length=40)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(max_length=800)
    title = models.CharField(max_length=60)
    
class Skills(models.Model):
    skill_name = models.CharField(max_length=40)
    description = models.TextField(max_length=120)
    example = models.URLField()