from pyexpat import model
from django.db import models

class WorkExperience(models.Model):
    company_name = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    title = models.TextField()