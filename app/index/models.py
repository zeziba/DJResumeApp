from distutils.text_file import TextFile
from django.db import models


class PersonalInfo(models.Model):
    first_name = models.CharField(max_length=40)
    middle_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=16)
    self_photo = models.URLField()

    def __str__(self) -> str:
        return f"{self.first_name}|{self.last_name}"


class WorkExperience(models.Model):
    personal = models.ForeignKey(to=PersonalInfo, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=40)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(max_length=800)
    title = models.CharField(max_length=60)

    def __str__(self) -> str:
        return f"{self.company_name}"


class Skills(models.Model):
    personal = models.ForeignKey(to=PersonalInfo, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=40)
    description = models.TextField(max_length=120)
    example = models.URLField()

    def __str__(self) -> str:
        return f"{self.skill_name}"


class FiveWs(models.Model):
    # ForeignKey will point to the person it belongs too
    personal = models.ForeignKey(to=PersonalInfo, on_delete=models.CASCADE)
    # We are <identity>
    identity = models.TextField(max_length=400)
    # We started <started>
    started = models.DateTimeField()
    # We work <location>
    location = models.CharField(max_length=120)
    # We strive <purpose>
    purpose = models.TextField(max_length=400)
    # We believe <how_its_done>
    how_its_done = models.TextField(max_length=400)

    def __str__(self) -> str:
        return f"{self.personal.last_name}"


class FactsForFiveWs(models.Model):

    class PriorityLevel(models.IntegerChoices):
        LOW = 0
        MED = 1
        High = 2

    five_ws = models.ForeignKey(to=FiveWs, on_delete=models.CASCADE)
    fact_score = models.IntegerField(choices=PriorityLevel.choices)
    factoid = models.TextField(max_length=120)

    def __str__(self) -> str:
        return f"{self.five_ws.personal.last_name}"
