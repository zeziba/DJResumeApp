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

class PersonalInfo(models.Model):
    first_name = models.CharField(max_length=40)
    middle_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=16)
    self_photo = models.URLField()
